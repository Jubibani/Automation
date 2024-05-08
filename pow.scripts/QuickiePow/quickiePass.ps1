# # Set the path to powershell.exe
# $powerShellExePath = "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

# Set the path to the ASCII art file
$asciiArtFilePath = "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation-Local\pow.scripts\QuickiePow\ASCII art\theRock.txt"

# Get the content of the ASCII art file
$asciiArt = Get-Content $asciiArtFilePath -Raw -Encoding UTF8

# Output the ASCII art
Write-Host $asciiArt

#* usable functions in here
function exit_delay {
    #im adding a delay. Displaying the count down with a for loop since powshell doesnt have a built-in countdown.
    Write-Host "implementing delay"
    $sleepDuration = 10
    for ($i = $sleepDuration; $i -ge 0; $i--) {
        Write-Host "Exit in $($i)s "
        Start-Sleep -Seconds 1
    }
    Write-Host "complete..."
}
# Prompt the user for password
$password = Read-Host "Enter password " -AsSecureString

# Convert secure string to plain text
$passwordInput = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))


# Check if the password is correct
if ($passwordInput -eq "HH211R") {
    Write-Host "Logging in as Jubibani..."
    # exit_delay 
    # Start a new PowerShell process to run quickiePow.ps1
    Start-Process -FilePath "powershell.exe" -ArgumentList "-ExecutionPolicy Bypass", "-File", "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation-Local\pow.scripts\QuickiePow\modules\quickiePow.ps1" -Wait -WindowStyle Hidden 
    # Start-Process -FilePath "powershell.exe" -ArgumentList "-ExecutionPolicy Bypass", "-File", "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\sampleTest.ps1" -Wait #?Testing Script
    Exit 1 #? this is only executed until StartProcess is finished Executed

    # $filePath = "C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation\pow.scripts\QuickiePow\quickiePass.ps1" #*Starting this line is to hide the Pass.ps1 file
    # $fileAttributes = (Get-Item $filePath).Attributes 
    # $fileAttributes = $fileAttributes -bor [System.IO.FileAttributes]::Hidden
    # Set-ItemProperty -Path $filePath -Name Attributes -Value $fileAttributes
} else {
    Write-Host "Wrong password. Exiting..."
    Exit 1
}
