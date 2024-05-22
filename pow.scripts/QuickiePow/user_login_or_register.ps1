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

# Call the function to find and run the target script
Find-And-Run-Script -filename "user_login_or_register.py"
Exit 1