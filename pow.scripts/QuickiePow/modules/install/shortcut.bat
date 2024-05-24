@echo off

rem Set the paths
set "source_file=C:\Quickie-Automation\pow.scripts\QuickiePow\user_login_or_register.ps1"
set "shortcut_path=%USERPROFILE%\Desktop\Quickie.lnk"
set "icon_path=C:\Quickie-Automation\pow.scripts\QuickiePow\logo\logoAppIco.ico"

rem Create the shortcut
set "executable=powershell.exe"
set "arguments=-windowstyle hidden -ExecutionPolicy Bypass -File "%source_file%""
set "description=Launch the Quickie script"

powershell -NoProfile -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%shortcut_path%'); $s.TargetPath = '%executable%'; $s.Arguments = '%arguments%'; $s.IconLocation = '%icon_path%'; $s.Description = '%description%'; $s.WindowStyle = 7; $s.Save()"

@REM echo Shortcut created on the desktop.
@REM pause