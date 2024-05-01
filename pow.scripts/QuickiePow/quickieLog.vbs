Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell.exe -ExecutionPolicy Bypass -File ""C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePow.ps1""", 0, True

'!This is from the quickiePass
' Start-Process -FilePath "powershell.exe" -ArgumentList "-ExecutionPolicy Bypass", "-File", "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePow.ps1" -Wait

'! This vbs file may not be needed
'? What happened? originally it is to hid any script file terminal. but a solution was found : -WindowStyle -Hidden
