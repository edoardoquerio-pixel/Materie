# RemoteEye — Monitoraggio & Controllo Remoto

## TL;DR

> **Quick Summary**: Applicazione .NET 10 in C# per il monitoraggio in tempo reale (tastiera, schermo, webcam, app attive) e il controllo remoto di un PC Windows, con architettura a connessione inversa.
>
> **Deliverables**:
> - **RemoteEye.Shared** — Libreria condivisa con protocollo di comunicazione binario e tipi messaggio
> - **RemoteEye.AgentService** — Windows Service (Session 0) per ciclo di vita, monitoraggio processi, connettività TCP
> - **RemoteEye.AgentHelper** — Processo utente (Session 1) per keyboard hook, screen capture, webcam, input remoto
> - **RemoteEye.Controller** — App Avalonia per dashboard remota con stream live e controllo
> - **RemoteEye.Shared.Tests** — Test xUnit TDD per protocollo e serializzazione
>
> **Estimated Effort**: **XL** (22 task principali + 4 final verification)
> **Parallel Execution**: **YES** — 5 wave parallele + wave finale
> **Critical Path**: Task 1 ? Task 4 ? Task 7 ? Task 12 ? Task 13 ? Task 15 ? Task 21 ? F1-F4 ? user ok

---

## Context

### Original Request
Creare un programma per monitorare tastiera, schermo, app aperte, controllare a distanza il PC, e fare streaming di schermo e webcam.

### Interview Summary
**Key Discussions**:
- **Scopo**: Esercitazione personale didattica — **non** uso malevolo
- **Architettura**: Connessione inversa (Agent ? Controller)
- **Agent**: Windows Service (Session 0) + Helper process (Session 1 utente)
- **Controller**: Applicazione Avalonia (cross-platform)
- **Streaming**: MJPEG — frame JPEG compressi a ~30fps su TCP
- **Webcam**: MediaCapture (WinRT API)
- **Compressione**: JPEG via System.Drawing
- **Test**: TDD con xUnit
- **Remote control**: Invio comandi da Controller ad Agent (mouse + tastiera remoti)

**Research Findings**:
- Workspace .NET: 11_Programmazione_DotNet_CSharp/03_Progetti/
- Stile codifica: ImplicitUsings, block namespace, Italiano/Inglese misto, classi *Biz
- Nessuna infrastruttura test esistente — xUnit da configurare
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
- [ ] dotnet build RemoteEye.sln — 0 errori, 0 warning
- [ ] dotnet test RemoteEye.sln — tutti i test PASS
- [ ] Controller avviato su PC A ? Agent su PC B si connette ? stream screen/webcam visibili live su Controller
- [ ] Controller può inviare input remoto (tastiera + mouse) che vengono eseguiti su Agent
- [ ] Keylog catturato da Agent e visualizzato in tempo reale su Controller
- [ ] App attive su Agent mostrate su Controller

### Must Have
- [ ] Protocollo TCP binario personalizzato (Header: Magic + Type + Length + Payload)
- [ ] TDD per Shared library (PacketSerializer, messaggi)
- [ ] Reverse connection: Agent ? Controller TCP
- [ ] MJPEG live streaming (~30fps) per schermo e webcam
- [ ] Remote input: keyboard + mouse da Controller ad Agent
- [ ] Windows Service + Helper process (Session 0/1 separation)
- [ ] Named Pipe per comunicazione Service ? Helper

### Must NOT Have (Guardrails)
- [ ] **NO crittografia** (v1 — rimandata a versione successiva)
- [ ] **NO file transfer** (v1 solo monitoraggio + controllo)
- [ ] **NO audio streaming** (solo video + input)
- [ ] **NO persistenza / auto-reconnect complesso** (riconnessione base ok)
- [ ] **NO multi-agent** (v1 supporta un agente per sessione Controller)
- [ ] **NO H.264/hardware encoding** — solo MJPEG

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — Tutta la verifica è eseguita da agenti.

### Test Decision
- **Infrastructure exists**: NO (da configurare)
- **Automated tests**: **TDD** — test-first per Shared library
- **Framework**: xUnit + Microsoft.NET.Test.Sdk
- **TDD workflow**: Ogni task di Shared segue RED (test fallisce) ? GREEN (implementazione minima) ? REFACTOR
- **Altri task**: test-after con xUnit dove fattibile

### QA Policy
- **Shared Library**: dotnet test
- **Agent Service**: PowerShell — install service, start/stop
- **Agent Helper**: PowerShell — verify process launch, named pipe
- **Controller UI**: dotnet build + run
- **Streaming**: Verifica JPEG frames ricevuti

---

## Execution Strategy

### Parallel Execution Waves

Wave 1 (Foundation — ALL parallel):
+-- [ 1] RemoteEye.sln + .csproj scaffolding [category: unspecified-high]
+-- [ 2] Shared: PacketType enum + message classes [category: unspecified-high]
+-- [ 3] Shared: PacketSerializer + TDD tests [category: unspecified-high]

Wave 2 (Agent Service — parallel dopo Wave 1):
+-- [ 4] AgentService: Windows Service lifecycle [category: deep]
+-- [ 5] AgentService: ProcessMonitor [category: deep]
+-- [ 6] AgentService: HelperProcessManager [category: deep]
+-- [ 7] AgentService: AgentConnector TCP client [category: unspecified-high]

Wave 3 (Agent Helper — parallel dopo Wave 2):
+-- [ 8] AgentHelper: Process + named pipe [category: unspecified-high]
+-- [ 9] AgentHelper: KeyboardHook SetWindowsHookEx [category: deep]
+-- [10] AgentHelper: ScreenCapturer CopyFromScreen [category: deep]
+-- [11] AgentHelper: WebcamCapturer MediaCapture [category: deep]
+-- [12] AgentHelper: RemoteInputReceiver SendInput [category: deep]

Wave 4 (Controller Network — parallel dopo Wave 3):
+-- [13] ControllerServer: TCP listener + multiplex [category: unspecified-high]
+-- [14] Controller: ConnectionManager + routing [category: unspecified-high]

Wave 5 (Controller UI — dipende da Wave 4 e Wave 3):
+-- [15] Controller: Avalonia scaffolding [category: visual-engineering]
+-- [16] Controller: Dashboard view [category: visual-engineering]
+-- [17] Controller: Screen stream viewer [category: visual-engineering]
+-- [18] Controller: Webcam stream viewer [category: visual-engineering]
+-- [19] Controller: Keylog display [category: visual-engineering]
+-- [20] Controller: Remote input panel [category: visual-engineering]
+-- [21] Controller: Settings + connection config [category: visual-engineering]

Wave FINAL (After ALL tasks — 4 parallel reviews):
+-- F1. Plan compliance audit [oracle]
+-- F2. Code quality + security review [unspecified-high]
+-- F3. Real manual QA integration test [unspecified-high]
+-- F4. Scope fidelity check [deep]

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
### [1] Solution scaffolding + .csproj references
- **Category**: unspecified-high
- **Description**: Create RemoteEye.sln with all 4 projects + test project. Configure .NET 10, ImplicitUsings, project references.
- **Files**: RemoteEye/RemoteEye.sln, RemoteEye.Shared/*.csproj, RemoteEye.AgentService/*.csproj, RemoteEye.AgentHelper/*.csproj, RemoteEye.Controller/*.csproj, RemoteEye.Shared.Tests/*.csproj
- **AC**: dotnet build RemoteEye.sln ? 0 errors

### [2] Shared: PacketType enum + message classes
- **Category**: unspecified-high
- **Description**: Define PacketType enum (ScreenFrame, WebcamFrame, Keylog, ActiveApp, RemoteInput, Command, Ack) and corresponding message classes with serializable properties.
- **Files**: RemoteEye.Shared/PacketType.cs, RemoteEye.Shared/Messages/*.cs
- **AC**: All classes compile, enum covers all required message types

### [3] Shared: PacketSerializer + TDD tests
- **Category**: unspecified-high
- **Description**: Binary protocol serializer: [Magic:2][Type:2][Length:4][Payload]. Write xUnit tests FIRST (TDD). Test serialize/deserialize roundtrip for each message type.
- **Files**: RemoteEye.Shared/Protocol/PacketHeader.cs, RemoteEye.Shared/Protocol/PacketSerializer.cs, RemoteEye.Shared.Tests/Protocol/PacketSerializerTests.cs
- **AC**: dotnet test ? all tests pass, roundtrip verified for all types

### [4] AgentService: Windows Service lifecycle
- **Category**: deep
- **Description**: Windows Service with ServiceBase. Install/uninstall scripts. OnStart starts helper process + TCP connector. OnStop clean shutdown.
- **Files**: RemoteEye.AgentService/Program.cs, RemoteEye.AgentService/AgentService.cs, RemoteEye.AgentService/install.ps1
- **AC**: Service installs, starts, stops without error

### [5] AgentService: ProcessMonitor
- **Category**: deep
- **Description**: Poll GetForegroundWindow + GetWindowText per finestra attiva. Enum processes via System.Diagnostics. Invia ActiveAppPacket periodico ad AgentConnector.
- **Files**: RemoteEye.AgentService/ProcessMonitor.cs
- **AC**: Detects foreground window changes, sends ActiveAppPacket

### [6] AgentService: HelperProcessManager
- **Category**: deep
- **Description**: Avvia AgentHelper.exe nella sessione utente (CreateProcessAsUser o scheduled task). Monitora processo helper, restart su crash. Gestisce named pipe server per comunicazione.
- **Files**: RemoteEye.AgentService/HelperProcessManager.cs
- **AC**: Helper process avviato, named pipe funzionante

### [7] AgentService: AgentConnector TCP client
- **Category**: unspecified-high
- **Description**: TCP client connessione inversa. Si connette a IP:Port del Controller. Invia pacchetti serializzati (da helper via pipe o da monitor). Riceve comandi dal Controller.
- **Files**: RemoteEye.AgentService/AgentConnector.cs
- **AC**: Connessione TCP stabilita, pacchetti inviati/ricevuti

### [8] AgentHelper: Process launch + named pipe protocol
- **Category**: unspecified-high
- **Description**: Console app che si connette al named pipe del Service. Ciclo eventi: riceve comandi dal pipe, cattura input/screen/webcam, invia dati al pipe. Hidden window.
- **Files**: RemoteEye.AgentHelper/Program.cs, RemoteEye.AgentHelper/ServicePipeClient.cs
- **AC**: Named pipe connection with Service established

### [9] AgentHelper: KeyboardHook
- **Category**: deep
- **Description**: SetWindowsHookEx WH_KEYBOARD_LL via P/Invoke. Cattura tasti premuti (down/up). Invia KeylogPacket attraverso named pipe.
- **Files**: RemoteEye.AgentHelper/KeyboardHook.cs
- **AC**: Key capture funzionante, pacchetti inviati

### [10] AgentHelper: ScreenCapturer
- **Category**: deep
- **Description**: Graphics.CopyFromScreen per cattura schermo. Encoding JPEG via System.Drawing.Stream ~30fps su named pipe. Controllo framerate.
- **Files**: RemoteEye.AgentHelper/ScreenCapturer.cs
- **AC**: Screen capture JPEG a ~30fps

### [11] AgentHelper: WebcamCapturer
- **Category**: deep
- **Description**: MediaCapture WinRT API. Cattura frame video ? SoftwareBitmap ? JPEG encoding. MJPEG stream su named pipe.
- **Files**: RemoteEye.AgentHelper/WebcamCapturer.cs
- **AC**: Webcam frame capture + JPEG encoding

### [12] AgentHelper: RemoteInputReceiver
- **Category**: deep
- **Description**: Riceve RemoteInputPacket dal pipe. SendInput API (P/Invoke) per injection tastiera + mouse. Supporta key down/up, mouse move/click/scroll.
- **Files**: RemoteEye.AgentHelper/RemoteInputReceiver.cs
- **AC**: Keyboard + mouse injection funzionante

### [13] ControllerServer: TCP listener
- **Category**: unspecified-high
- **Description**: TCP server in ascolto. Accetta connessione Agent. Multiplex: stream separati per screen/webcam/keylog/app su canali logici. Dispatch pacchetti ai ViewModel.
- **Files**: RemoteEye.Controller/Network/ControllerServer.cs
- **AC**: TCP listener attivo, pacchetti ricevuti e smistati

### [14] Controller: ConnectionManager + routing
- **Category**: unspecified-high
- **Description**: Gestisce stato connessione Agent (connected/disconnected). Route pacchetti in entrata al ViewModel corretto. Send comandi all'Agent.
- **Files**: RemoteEye.Controller/Network/ConnectionManager.cs
- **AC**: Connessione gestita, routing funzionante

### [15] Controller: Avalonia scaffolding
- **Category**: visual-engineering
- **Description**: Progetto Avalonia con MainWindow. TabControl per navigazione (Dashboard, Screen, Webcam, Keylog, Remote Input, Settings). MVVM pattern.
- **Files**: RemoteEye.Controller/*.axaml, RemoteEye.Controller/ViewModels/*.cs, RemoteEye.Controller/App.axaml
- **AC**: UI si avvia, tab navigation funziona

### [16] Controller: Dashboard view
- **Category**: visual-engineering
- **Description**: Stato connessione (IP, connected since), active app list, statistiche (fps, pacchetti/s), pulsanti connect/disconnect.
- **Files**: RemoteEye.Controller/Views/DashboardView.axaml, RemoteEye.Controller/ViewModels/DashboardViewModel.cs
- **AC**: Dashboard mostra stato connessione e app attive

### [17] Controller: Screen stream viewer
- **Category**: visual-engineering
- **Description**: Riceve ScreenFramePacket ? decoded JPEG ? Image control. Refresh a 30fps. Indicatore FPS.
- **Files**: RemoteEye.Controller/Views/ScreenView.axaml, RemoteEye.Controller/ViewModels/ScreenViewModel.cs
- **AC**: Stream screen live visibile

### [18] Controller: Webcam stream viewer
- **Category**: visual-engineering
- **Description**: Riceve WebcamFramePacket ? decoded JPEG ? Image control. Refresh a 30fps. Toggle on/off.
- **Files**: RemoteEye.Controller/Views/WebcamView.axaml, RemoteEye.Controller/ViewModels/WebcamViewModel.cs
- **AC**: Stream webcam live visibile

### [19] Controller: Keylog display
- **Category**: visual-engineering
- **Description**: Riceve KeylogPacket ? TextBlock/ListBox scrollabile. Timestamp per ogni keystroke. Pulsante clear.
- **Files**: RemoteEye.Controller/Views/KeylogView.axaml, RemoteEye.Controller/ViewModels/KeylogViewModel.cs
- **AC**: Keylog visualizzato in tempo reale

### [20] Controller: Remote input panel
- **Category**: visual-engineering
- **Description**: Pannello con: text input per digitazione remota, simulazione tasti speciali (Enter, Tab, Esc, arrows), area mouse (click simulator, coordinate). Invia RemoteInputPacket.
- **Files**: RemoteEye.Controller/Views/RemoteInputView.axaml, RemoteEye.Controller/ViewModels/RemoteInputViewModel.cs
- **AC**: Input remoto inviato, eseguito su Agent

### [21] Controller: Settings + connection config
- **Category**: visual-engineering
- **Description**: Config IP/Porta del listener TCP. Auto-start option. Salva settings in JSON. About box.
- **Files**: RemoteEye.Controller/Views/SettingsView.axaml, RemoteEye.Controller/ViewModels/SettingsViewModel.cs
- **AC**: Settings salvati e caricati

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