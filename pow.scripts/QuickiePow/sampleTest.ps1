Write-Host "Testing"
#! For Testing only
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


exit_delay