
    #change it to whatever you put the ascii art in
    $asciiArtFilePath = "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\ASCII art\theRock.txt"
    $asciiArt = Get-Content $asciiArtFilePath -Raw -Encoding UTF8

    # Output the ASCII art
    Write-Host $asciiArt
    $password = Read-Host "Enter password " -AsSecureString
    $passwordInput = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))
    
    if ($passwordInput -eq "HH211R") {
        Write-Host "logging in as Jubibani"
        Start-Process -FilePath powershell.exe -ArgumentList "-File 'C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePow.ps1'" -Wait
        
        
    } else {
        Write-Host "Wrong password. Exiting..."
        Exit
    }