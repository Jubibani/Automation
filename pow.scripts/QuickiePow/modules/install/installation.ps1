Set-ExecutionPolicy Bypass -Scope Process
# Install required Python packages
Write-Host "Installing required Python packages..."
python -m pip install --user seleniumbase
python -m pip install --user pandas
python -m pip install --user cryptography
python -m pip install --user bcrypt
Write-Host "Package installation completed."

# Run the shortcut.bat file
$batFilePath = "C:\Quickie-Automation\pow.scripts\QuickiePow\modules\install\shortcut.bat"
Start-Process $batFilePath

Write-Host "Quickie sent to Desktop."

Read-Host "Press Enter to exit"