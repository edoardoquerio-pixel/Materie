# RemoteEye � Monitoraggio & Controllo Remoto

## TL;DR

> **Quick Summary**: Applicazione .NET 10 in C# per il monitoraggio in tempo reale (tastiera, schermo, webcam, app attive) e il controllo remoto di un PC Windows, con architettura a connessione inversa.
>
> **Deliverables**:
> - **RemoteEye.Shared** � Libreria condivisa con protocollo di comunicazione binario e tipi messaggio
> - **RemoteEye.AgentService** � Windows Service (Session 0) per ciclo di vita, monitoraggio processi, connettivit� TCP
> - **RemoteEye.AgentHelper** � Processo utente (Session 1) per keyboard hook, screen capture, webcam, input remoto
> - **RemoteEye.Controller** � App Avalonia per dashboard remota con stream live e controllo
> - **RemoteEye.Shared.Tests** � Test xUnit TDD per protocollo e serializzazione
>
> **Estimated Effort**: **XL** (22 task principali + 4 final verification)
> **Parallel Execution**: **YES** � 5 wave parallele + wave finale
> **Critical Path**: Task 1 ? Task 4 ? Task 7 ? Task 12 ? Task 13 ? Task 15 ? Task 21 ? F1-F4 ? user ok

---

## Context

### Original Request
Creare un programma per monitorare tastiera, schermo, app aperte, controllare a distanza il PC, e fare streaming di schermo e webcam.

### Interview Summary
**Key Discussions**:
- **Scopo**: Esercitazione personale didattica � **non** uso malevolo
- **Architettura**: Connessione inversa (Agent ? Controller)
- **Agent**: Windows Service (Session 0) + Helper process (Session 1 utente)
- **Controller**: Applicazione Avalonia (cross-platform)
- **Streaming**: MJPEG � frame JPEG compressi a ~30fps su TCP
- **Webcam**: MediaCapture (WinRT API)
- **Compressione**: JPEG via System.Drawing
- **Test**: TDD con xUnit
- **Remote control**: Invio comandi da Controller ad Agent (mouse + tastiera remoti)

**Research Findings**:
- Workspace .NET: 11_Programmazione_DotNet_CSharp/03_Progetti/
- Stile codifica: ImplicitUsings, block namespace, Italiano/Inglese misto, classi *Biz
- Nessuna infrastruttura test esistente � xUnit da configurare
- **Project root**: privato/programma/RemoteEye/ (sotto Materie)

---

## Work Objectives

### Core Objective
Realizzare un sistema client-server di monitoraggio e controllo remoto per Windows, composto da un Agent (Service + Helper) e un Controller (Avalonia GUI), comunicanti via TCP con protocollo binario personalizzato.

### Concrete Deliverables
- .sln e progetti .NET 10 con ImplicitUsings abilitato
- RemoteEye.Shared: PacketType enum, classi messaggio, PacketHeader, PacketSerializer
- RemoteEye.AgentService: Windows Service con installazione, ProcessMonitor, AgentConnector, HelperProcessManager
- RemoteEye.AgentHelper: KeyboardHook, ScreenCapturer, WebcamCapturer, RemoteInputReceiver
- RemoteEye.Controller: App Avalonia con dashboard, stream viewer, keylog, remote input panel
- RemoteEye.Shared.Tests: Test xUnit in stile TDD

### Definition of Done
- [x] dotnet build RemoteEye.sln — 0 errori, 0 warning
- [x] dotnet test RemoteEye.sln — tutti i test PASS
- [x] Controller avviato su PC A — Agent su PC B si connette — stream screen/webcam visibili live su Controller
- [x] Controller puo inviare input remoto (tastiera + mouse) che vengono eseguiti su Agent
- [x] Keylog catturato da Agent e visualizzato in tempo reale su Controller
- [x] App attive su Agent mostrate su Controller

### Must Have
- [x] Protocollo TCP binario personalizzato (Header: Magic + Type + Length + Payload)
- [x] TDD per Shared library (PacketSerializer, messaggi)
- [x] Reverse connection: Agent → Controller TCP
- [x] MJPEG live streaming (~30fps) per schermo e webcam
- [x] Remote input: keyboard + mouse da Controller ad Agent
- [x] Windows Service + Helper process (Session 0/1 separation)
- [x] Named Pipe per comunicazione Service ↔ Helper

### Must NOT Have (Guardrails)
- [x] **NO crittografia** (v1 rimandata a versione successiva)
- [x] **NO file transfer** (v1 solo monitoraggio + controllo)
- [x] **NO audio streaming** (solo video + input)
- [x] **NO persistenza / auto-reconnect complesso** (riconnessione base ok)
- [x] **NO multi-agent** (v1 supporta un agente per sessione Controller)
- [x] **NO H.264/hardware encoding** — solo MJPEG

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** � Tutta la verifica � eseguita da agenti.

### Test Decision
- **Infrastructure exists**: NO (da configurare)
- **Automated tests**: **TDD** � test-first per Shared library
- **Framework**: xUnit + Microsoft.NET.Test.Sdk
- **TDD workflow**: Ogni task di Shared segue RED (test fallisce) ? GREEN (implementazione minima) ? REFACTOR
- **Altri task**: test-after con xUnit dove fattibile

### QA Policy
- **Shared Library**: dotnet test
- **Agent Service**: PowerShell � install service, start/stop
- **Agent Helper**: PowerShell � verify process launch, named pipe
- **Controller UI**: dotnet build + run
- **Streaming**: Verifica JPEG frames ricevuti

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Foundation � ALL parallel):
+-- [ 1] RemoteEye.sln + .csproj scaffolding [category: unspecified-high]
+-- [ 2] Shared: PacketType enum + message classes [category: unspecified-high]
+-- [ 3] Shared: PacketSerializer + TDD tests [category: unspecified-high]

Wave 2 (Agent Service � parallel dopo Wave 1):
+-- [ 4] AgentService: Windows Service lifecycle [category: deep]
+-- [ 5] AgentService: ProcessMonitor [category: deep]
+-- [ 6] AgentService: HelperProcessManager [category: deep]
+-- [ 7] AgentService: AgentConnector TCP client [category: unspecified-high]

Wave 3 (Agent Helper � parallel dopo Wave 2):
+-- [ 8] AgentHelper: Process + named pipe [category: unspecified-high]
+-- [ 9] AgentHelper: KeyboardHook SetWindowsHookEx [category: deep]
+-- [10] AgentHelper: ScreenCapturer CopyFromScreen [category: deep]
+-- [11] AgentHelper: WebcamCapturer MediaCapture [category: deep]
+-- [12] AgentHelper: RemoteInputReceiver SendInput [category: deep]

Wave 4 (Controller Network � parallel dopo Wave 3):
+-- [13] ControllerServer: TCP listener + multiplex [category: unspecified-high]
+-- [14] Controller: ConnectionManager + routing [category: unspecified-high]

Wave 5 (Controller UI � dipende da Wave 4 e Wave 3):
+-- [15] Controller: Avalonia scaffolding [category: visual-engineering]
+-- [16] Controller: Dashboard view [category: visual-engineering]
+-- [17] Controller: Screen stream viewer [category: visual-engineering]
+-- [18] Controller: Webcam stream viewer [category: visual-engineering]
+-- [19] Controller: Keylog display [category: visual-engineering]
+-- [20] Controller: Remote input panel [category: visual-engineering]
+-- [21] Controller: Settings + connection config [category: visual-engineering]

Wave FINAL (After ALL tasks - 4 parallel reviews):
+-- [x] F1. Plan compliance audit [oracle]
+-- [x] F2. Code quality + security review [unspecified-high]
+-- [x] F3. Real manual QA integration test [unspecified-high]
+-- [x] F4. Scope fidelity check [deep]

### Dependency Matrix

| Task | Dipende da | Blocca |
|------|-----------|--------|
| 1 | - | 3-21 |
| 2 | - | 3 |
| 3 | 1, 2 | 7, 13 |
| 4 | 1 | 6, 7 |
| 5 | 1 | 7 |
| 6 | 4 | 8 |
| 7 | 3, 4 | 13 |
| 8 | 6 | 9-12 |
| 9 | 8 | - |
| 10 | 8 | - |
| 11 | 8 | - |
| 12 | 8 | 20 |
| 13 | 3, 7, 14 | 16-21 |
| 14 | 1 | 13 |
| 15 | 1 | 16-21 |
| 16 | 13, 15 | - |
| 17 | 13, 15 | - |
| 18 | 13, 15 | - |
| 19 | 13, 15 | - |
| 20 | 12, 13, 15 | - |
| 21 | 15 | - |
| F1-F4 | All tasks | user ok |

---

## TODOs

- [x] 1. Solution scaffolding + .csproj references
- [x] 2. Shared: PacketType enum + message classes
- [x] 3. Shared: PacketSerializer + TDD tests
- [x] 4. AgentService: Windows Service lifecycle
- [x] 5. AgentService: ProcessMonitor
- [x] 6. AgentService: HelperProcessManager
- [x] 7. AgentService: AgentConnector TCP client
- [x] 8. AgentHelper: Process launch + named pipe protocol
- [x] 9. AgentHelper: KeyboardHook
- [x] 10. AgentHelper: ScreenCapturer
- [x] 11. AgentHelper: WebcamCapturer
- [x] 12. AgentHelper: RemoteInputReceiver
- [x] 13. ControllerServer: TCP listener
- [x] 14. Controller: ConnectionManager + routing
- [x] 15. Controller: Avalonia scaffolding
- [x] 16. Controller: Dashboard view
- [x] 17. Controller: Screen stream viewer
- [x] 18. Controller: Webcam stream viewer
- [x] 19. Controller: Keylog display
- [x] 20. Controller: Remote input panel
- [x] 21. Controller: Settings + connection config

---

## Final Verification Wave (F1-F4)

Eseguito DOPO il completamento di tutti i task 1-21.

### F1. Plan Compliance Audit
- **Agent**: oracle
- **Scope**: Verifica che tutti i deliverable del piano siano stati realizzati. Confronta requirements vs implementation.

### F2. Code Quality + Security Review
- **Agent**: unspecified-high
- **Scope**: Code review: error handling, disposability, thread safety, edge cases. Security: input injection, named pipe security, TCP encryption absence.

### F3. Real Manual QA Integration Test
- **Agent**: unspecified-high
- **Scope**: Build test ? Service install ? Helper launch ? TCP connect ? Screen stream ? Webcam stream ? Keylog ? Remote input ? Clean shutdown.

### F4. Scope Fidelity Check
- **Agent**: deep
- **Scope**: Verifica MUST NOT HAVE guardrails (no crypto, no file transfer, no audio, no H.264). Segnala scope creep.

---

## Success Criteria (presentati all'utente)

Dopo F1-F4, presentare report sintetico:
- **Build**: ? / ?
- **Test**: N pass / N total
- **Stream screen**: ? / ?
- **Stream webcam**: ? / ?
- **Keylog**: ? / ?
- **Remote input**: ? / ?
- **App tracking**: ? / ?
- **Scope creep**: ? / ? (elenco se presente)
- **Blocking issues**: numero
- **Ready for user**: ? / ?