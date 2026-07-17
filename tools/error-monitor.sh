#!/usr/bin/env bash
# Error Monitor Agent Launcher (bash version for Linux/macOS/WSL)
# Usage: ./error-monitor.sh "command to run" [--auto-fix] [--max-retries N] [--cwd /path] [--log-file /path]

set -euo pipefail

CMD=""
CWD="$(pwd)"
AUTO_FIX=false
MAX_RETRIES=3
POLL_INTERVAL=0.5
NOTIFY=true
LOG_FILE=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --auto-fix) AUTO_FIX=true; shift ;;
        --max-retries) MAX_RETRIES="$2"; shift 2 ;;
        --cwd) CWD="$2"; shift 2 ;;
        --no-notify) NOTIFY=false; shift ;;
        --log-file) LOG_FILE="$2"; shift 2 ;;
        --poll-interval) POLL_INTERVAL="$2"; shift 2 ;;
        *) CMD="$1"; shift ;;
    esac
done

if [[ -z "$CMD" ]]; then
    echo "Usage: $0 \"command\" [--auto-fix] [--max-retries N] [--cwd /path] [--log-file /path]"
    exit 1
fi

error_patterns=(
    '(?i)error|errore|exception|traceback|fail|failed|error:|panic|fatal|abort'
    '(?i)exit code [1-9]'
    '(?i)command not found|not found|no such file'
    '(?i)permission denied|access denied|unauthorized'
    '(?i)timeout|timed out'
    '(?i)syntax error|parse error|compilation error'
    '(?i)module not found|import error|cannot find module'
    '(?i)connection refused|econnrefused|eaddrinuse'
)

log() {
    local level="$1"; shift
    local msg="[$(date '+%H:%M:%S')] [$level] $*"
    echo "$msg"
    [[ -n "$LOG_FILE" ]] && echo "$msg" >> "$LOG_FILE"
}

notify() {
    [[ "$NOTIFY" == true ]] || return
    if command -v notify-send &>/dev/null; then
        notify-send "Error Monitor" "$1" -u critical
    elif command -v osascript &>/dev/null; then
        osascript -e "display notification \"$2\" with title \"$1\""
    fi
}

test_error_line() {
    local line="$1"
    for pattern in "${error_patterns[@]}"; do
        if [[ "$line" =~ $pattern ]]; then
            return 0
        fi
    done
    return 1
}

extract_context() {
    local -n lines_ref=$1
    local error_idx=$2
    local context=${3:-5}
    local start=$((error_idx - context))
    local end=$((error_idx + context))
    (( start < 0 )) && start=0
    (( end >= ${#lines_ref[@]} )) && end=$((${#lines_ref[@]} - 1))
    for ((i=start; i<=end; i++)); do
        echo "${lines_ref[i]}"
    done
}

classify_error() {
    local block="$1"
    if [[ "$block" =~ (?i)syntax|parse|compilation ]]; then echo "syntax"; return; fi
    if [[ "$block" =~ (?i)module not found|import error|cannot find module|missing dependency ]]; then echo "dependency"; return; fi
    if [[ "$block" =~ (?i)permission|access denied|unauthorized ]]; then echo "permission"; return; fi
    if [[ "$block" =~ (?i)connection refused|econnrefused|eaddrinuse|network|dns ]]; then echo "network"; return; fi
    if [[ "$block" =~ (?i)timeout|timed out ]]; then echo "timeout"; return; fi
    if [[ "$block" =~ (?i)test.*fail|assertion|expected.*actual ]]; then echo "test-fail"; return; fi
    if [[ "$block" =~ (?i)file not found|no such file|path ]]; then echo "config"; return; fi
    echo "runtime"
}

locate_file_in_error() {
    local block="$1"
    if [[ "$block" =~ ([A-Za-z]:[^[:space:]:]+|[./][^[:space:]:]+):([0-9]+) ]]; then
        echo "${BASH_REMATCH[1]}:${BASH_REMATCH[2]}"
        return
    fi
    if [[ "$block" =~ at[[:space:]]+([^[:space:]:]+):([0-9]+) ]]; then
        echo "${BASH_REMATCH[1]}:${BASH_REMATCH[2]}"
        return
    fi
    if [[ "$block" =~ \(([^[:space:]:]+):([0-9]+)\) ]]; then
        echo "${BASH_REMATCH[1]}:${BASH_REMATCH[2]}"
        return
    fi
    echo ""
}

propose_fix() {
    local category="$1"
    local location="$2"
    case "$category" in
        syntax)      echo "Check syntax at $location — missing bracket/quote/semicolon?" ;;
        dependency)  echo "Run package install (npm install / dotnet restore / pip install -r requirements.txt)" ;;
        permission)  echo "chmod +x or run with correct permissions" ;;
        network)     echo "Start required service (docker/db/api) or check port availability" ;;
        timeout)     echo "Increase timeout or fix blocking call" ;;
        test-fail)   echo "Fix assertion or test setup at $location" ;;
        config)      echo "Verify config file exists at correct path / set required env vars" ;;
        *)           echo "Inspect $location — likely null ref or logic error" ;;
    esac
}

# MAIN
log "INFO" "Starting monitor for: $CMD"
log "INFO" "CWD: $CWD | AutoFix: $AUTO_FIX | MaxRetries: $MAX_RETRIES"

retry_count=0
full_output=()

while (( retry_count <= MAX_RETRIES )); do
    if (( retry_count > 0 )); then
        log "RETRY" "=== RETRY $retry_count/$MAX_RETRIES ==="
    fi

    cd "$CWD"
    error_detected=false
    first_error_block=""
    exit_code=0
    all_lines=()

    # Run command and capture output line by line
    while IFS= read -r line; do
        echo "[OUT] $line"
        all_lines+=("[OUT] $line")
        full_output+=("[OUT] $line")
    done < <(eval "$CMD" 2>&1; exit_code=$?; exit $exit_code) || true

    log "INFO" "Process exited with code: $exit_code"

    # Scan for errors
    for ((i=0; i<${#all_lines[@]}; i++)); do
        if test_error_line "${all_lines[i]}"; then
            error_detected=true
            first_error_block=$(extract_context all_lines "$i")
            break
        fi
    done

    if (( exit_code == 0 )) && [[ "$error_detected" == false ]]; then
        log "SUCCESS" "Command completed cleanly"
        notify "Error Monitor" "Command succeeded: $CMD"
        exit 0
    fi

    if [[ "$error_detected" == true ]] || (( exit_code != 0 )); then
        log "ERROR" "ERROR DETECTED (exit=$exit_code)"
        notify "Error Monitor: Error detected" "Exit code: $exit_code. Analyzing..."

        category=$(classify_error "$first_error_block")
        location=$(locate_file_in_error "$first_error_block")

        log "INFO" "ANALYSIS: Category=$category"
        [[ -n "$location" ]] && log "INFO" "LOCATION: $location"

        fix=$(propose_fix "$category" "$location")
        log "FIX" "PROPOSED FIX: $fix"

        if [[ "$AUTO_FIX" == true ]] && [[ -n "$location" ]]; then
            log "WARN" "AUTO-FIX: Not yet implemented — would edit $location"
        fi

        ((retry_count++))
        if (( retry_count > MAX_RETRIES )); then
            log "FATAL" "MAX RETRIES EXCEEDED"
            report="=== ERROR MONITOR REPORT ===
Command: $CMD
CWD: $CWD
Exit Code: $exit_code
Retries: $MAX_RETRIES
Category: $category
Location: $location
Proposed Fix: $fix
Full Output (last 200 lines):
$(printf '%s\n' "${full_output[@]: -200}")"
            [[ -n "$LOG_FILE" ]] && echo "$report" >> "$LOG_FILE"
            notify "Error Monitor: FAILED" "Max retries reached. See log: $LOG_FILE"
            exit 1
        fi

        log "WAIT" "Waiting 2s before retry..."
        sleep 2
    fi
done

log "FATAL" "Monitor stopped unexpectedly"
exit 1