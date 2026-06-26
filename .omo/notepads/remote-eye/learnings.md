## 2026-06-19: KeyboardHook.cs created

- Created RemoteEye.AgentHelper/KeyboardHook.cs � static class with Start(Pipe)/Stop()
- Uses WH_KEYBOARD_LL via P/Invoke (SetWindowsHookEx, UnhookWindowsHookEx, CallNextHookEx)
- KBDLLHOOKSTRUCT defined for lParam parsing on key down/up events
- On each key event: creates KeylogPacket(Timestamp, VirtualKeyCode, KeyChar, KeyDown) and sends via Pipe.SendToServiceAsync()
- Background thread runs manual GetMessage loop (no Windows.Forms dependency)
- MapVirtualKey(MAPVK_VK_TO_CHAR) used for virtual key ? char conversion
- Delegate stored as static field (_hookProc) to prevent GC collection
- Updated Program.cs: uncommented KeyboardHook.Start(Pipe); line
- Key decisions: no Windows Forms dependency, manual message pump with GetMessage, null passed to GetModuleHandle for current process handle



## 2026-06-19 � RemoteInputReceiver implementation

- Created RemoteEye.AgentHelper/RemoteInputReceiver.cs � static class with Start/Stop pattern
- Subscribes to ServicePipeClient.OnPacketReceived event, filters for RemoteInputPacket
- Deserializes raw bytes using PacketSerializer.Deserialize() then dispatches based on InputType
- Supports: KeyDown/KeyUp (virtual key + scan code via KEYBDINPUT), MouseMove (MOUSEINPUT dx/dy), MouseDown/Up/Click (left/right/middle/X buttons), MouseScroll (wheel delta), Text (unicode KEYBDINPUT per char)
- Uses SendInput P/Invoke from user32.dll with properly laid-out INPUT/InputUnion/MOUSEINPUT/KEYBDINPUT/HARDWAREINPUT structs
- Follows project conventions: no using directives, fully qualified external types, file-scoped namespace
- Updated Program.cs line 24: RemoteInputReceiver.Start(Pipe); now active
- Pre-existing build issues (NETSDK1130 WinMD, missing System.Drawing in ScreenCapturer.cs, missing AgentConnection in Controller) � unrelated to this change
## 2026-06-19 - WebcamCapturer module created

### Files created/modified
- Created: RemoteEye.AgentHelper/WebcamCapturer.cs — static class with Start(ServicePipeClient)/Stop()
- Modified: RemoteEye.AgentHelper/RemoteEye.AgentHelper.csproj — added WinRT/Windows targets, global usings
- Modified: RemoteEye.AgentHelper/Program.cs — uncommented WebcamCapturer.Start(Pipe)

### Architecture
- STA thread for MediaCapture initialization (required by WinRT)
- Capture loop at ~30fps via GetPreviewFrameAsync() + Thread.Sleep(33)
- Frame pipeline: VideoFrame → SoftwareBitmap → SoftwareBitmap.Convert(Bgra8) → BitmapEncoder(Jpeg) → byte[]
- Packet sent via PacketSerializer.Serialize(WebcamFramePacket) through named pipe

### .csproj requirements for WinRT on .NET 10
- TargetFramework: net10.0-windows10.0.19041.0 — Windows SDK target for WinRT interop
- UseWinUI: false — explicitly disable WinUI (not needed)
- Do NOT add Microsoft.Windows.SDK.Contracts NuGet — conflicts with .NET 10 built-in WinRT projection (NETSDK1130)
- WinRT types are available automatically via the Windows TFM
- Avoid global using for Windows.Storage.Streams — conflicts with System.Buffer in ServicePipeClient
- Use fully qualified Windows.Storage.Streams.InMemoryRandomAccessStream / DataReader instead

### Key gotchas
- SendToServiceAsync returns Task — call .GetAwaiter().GetResult() directly, NOT .AsTask(). AsTask() is only for WinRT IAsyncAction/IAsyncOperation
- UseWindowsForms=true causes Timer ambiguity in ScreenCapturer.cs — fixed with fully qualified System.Threading.Timer
## ScreenCapturer Implementation (2026-06-19)

- ScreenCapturer.cs created as static class with Start(ServicePipeClient) / Stop() pattern.
- Uses System.Threading.Timer at 33ms interval for ~30fps capture.
- Graphics.CopyFromScreen captures primary screen via System.Windows.Forms.Screen.PrimaryScreen.Bounds.
- JPEG encoding at quality 85 via System.Drawing.Imaging.ImageCodecInfo + EncoderParameters.
- ImageCodecInfo requires fully qualified name on `net10.0-windows10.0.19041.0` TFM.
- Packages added: System.Drawing.Common (10.*), System.Windows.Forms (for Screen).
- Global Using directives added: System.Drawing, System.Drawing.Imaging.
