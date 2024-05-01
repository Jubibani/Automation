# # Set the path to powershell.exe
# $powerShellExePath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

# Set the path to the ASCII art file
$asciiArtFilePath = "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\ASCII art\theRock.txt"

# Get the content of the ASCII art file
$asciiArt = Get-Content $asciiArtFilePath -Raw -Encoding UTF8

# Output the ASCII art
Write-Host $asciiArt

# Prompt the user for password
$password = Read-Host "Enter password " -AsSecureString

# Convert secure string to plain text
$passwordInput = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))

# Check if the password is correct
if ($passwordInput -eq "HH211R") {
    Write-Host "Logging in as Jubibani"
    # Start a new PowerShell process to run quickiePow.ps1
    # Start-Process -FilePath $powerShellExePath -ArgumentList "-ExecutionPolicy Bypass", "-File 'C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePow.ps1'"
    Start-Process -FilePath "powershell.exe" -ArgumentList "-ExecutionPolicy Bypass", "-File", "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePow.ps1" -Wait
} else {
    Write-Host "Wrong password. Exiting..."
    Exit 1
}