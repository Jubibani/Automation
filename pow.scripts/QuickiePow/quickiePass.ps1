# Function to find and display the ASCII art
function Find-And-Display-ASCII {
    param (
        [string]$filename
    )

    # Iterate over all directories and subdirectories
    Get-ChildItem -Path "C:\Quickie-Automation" -Recurse -File | ForEach-Object {
        if ($_.Name -eq $filename) {
            # Construct the full path to the file
            $filePath = $_.FullName
            # Get the content of the ASCII art file
            $asciiArt = Get-Content $filePath -Raw -Encoding UTF8
            # Output the ASCII art
            Write-Host $asciiArt
            return
        }
    }

}

# Call the function to find and display the ASCII art
Find-And-Display-ASCII -filename "theRock.txt"
# Function to find and run the target script
function Find-And-Run-Script {
    param (
        [string]$filename
    )

    # Iterate over all directories and subdirectories
    $fileFound = $false
    Get-ChildItem -Path "C:\Quickie-Automation" -Recurse -File | ForEach-Object {
        if ($_.Name -eq $filename) {
            # Construct the full path to the script
            $scriptPath = $_.FullName
            # Run the script as a separate process
            Start-Process -FilePath "python.exe" -ArgumentList $scriptPath -Wait -NoNewWindow
            Write-Host "File found"
            return
        }
    }

    if (-not $fileFound) {
        Write-Host "Python script file not found."
    }
}

# Usable functions in here
function exit_delay {
    # Adding a delay. Displaying the countdown with a for loop since PowerShell doesn't have a built-in countdown.
    Write-Host "Implementing delay"
    $sleepDuration = 10
    for ($i = $sleepDuration; $i -ge 0; $i--) {
        Write-Host "Exit in $($i)s "
        Start-Sleep -Seconds 1
    }
    Write-Host "Complete..."
}

# Prompt the user for password
$passwordInput = Read-Host "Enter password" -AsSecureString

# Convert secure string to plain text
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($passwordInput)
$plainPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)
[System.Runtime.InteropServices.Marshal]::ZeroFreeBSTR($BSTR)

# Check if the password is correct
if ($plainPassword -eq "HH211R") {
    Write-Host "Logging in as Jubibani..."
    # Call the function to find and run the target script
    Find-And-Run-Script -filename "quickieLog.py"
    Exit 1
} else {
    Write-Host "Wrong password. Exiting..."
    Exit 1
}
