# Import Selenium WebDriver module
Import-Module Selenium
Add-Type -AssemblyName System.Threading

Write-Host "Quickie Passed!"
# Set the path to ChromeDriver (change it if you have to)
$chromeDriverPath = "C:\selenium-selenium-4.18.0"
# Start ChromeDriver process
Start-Process -FilePath "C:\selenium-selenium-4.18.0\chromedriver.exe" -WindowStyle Hidden
# # Create ChromeOptions instance and set unhandledPromptBehavior to ignore
$chromeOptions = New-Object OpenQA.Selenium.Chrome.ChromeOptions
# $chromeOptions.AddArgument("--unhandledPromptBehavior=ignore")
$chromeOptions.AddArgument("--incognito")  # Added incognito argument here

# Add user agent and disable automation flags to mimic a real user
$chromeOptions.AddArgument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36")
$chromeOptions.AddArgument("--disable-blink-features=AutomationControlled")


#* usable functions in here
function delay {
    #im adding a delay. Displaying the count down with a for loop since powshell doesnt have a built-in countdown.
    Write-Host "implementing delay"
    $sleepDuration = 2
    for ($i = $sleepDuration; $i -ge 0; $i--) {
        Write-Host "Waiting... $($i)s remaining"
        Start-Sleep -Seconds 1
    }
    Write-Host "done delaying"
}
function switchWindow {
    # Switch to the newly opened window or frame, also this will act as the delay
$driver.SwitchTo().Window($driver.WindowHandles[-1])
}
function Wait-WebDriverElement {
    param (
        [Parameter(Mandatory = $true)]
        [OpenQA.Selenium.IWebDriver]$Driver,

        [Parameter(Mandatory = $true)]
        [System.Management.Automation.ScriptBlock]$ScriptBlock
    )

    $wait = New-Object OpenQA.Selenium.Support.UI.WebDriverWait -ArgumentList $Driver, ([timespan]::FromSeconds(30))
    $element = $wait.Until([System.Func[OpenQA.Selenium.IWebDriver, OpenQA.Selenium.IWebElement]]{ $ScriptBlock.Invoke($args[0]) })
    return $element
}

#* variables to be used
    # Implement explicit wait for the email input field to be present
    $wait = New-Object OpenQA.Selenium.Support.UI.WebDriverWait -ArgumentList $driver, ([timespan]::FromSeconds(30))
#*functions to be called

# # Create a new ChromeDriver instance with ChromeOptions
$driver = New-Object OpenQA.Selenium.Chrome.ChromeDriver($chromeDriverPath, $chromeOptions)
function loginToUcCanvasUsingQuickie{
    $driver.Navigate().GoToUrl("https://uc-bcf.instructure.com/") 
    
    #implement delay to wait for booting process
    delay
    Write-Host "delaying"
    #implicit wait for up to 10 seconds
    $driver.Manage().Timeouts().ImplicitWait = (New-TimeSpan -Seconds 10)
    #we enter the school email for our canvas
    Write-Host "Entering School Email"
    $emailSchool = Wait-WebDriverElement -Driver $driver -ScriptBlock { param($driver) $driver.FindElementById("i0116") }
    $emailSchool.SendKeys("...") #!! careful here

    #click next button after entering my gmail
    Write-Host "Clicking Next Button"
    # $enterNextButton = $wait.Until({$driver.FindElementById("idSIButton9") })
    $enterNextButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { param($driver) $driver.FindElementById("idSIButton9") }
    $enterNextButton.Click()

    delay
    Write-Host "delaying"
    #implicit wait for up to 10 seconds
    $driver.Manage().Timeouts().ImplicitWait = (New-TimeSpan -Seconds 10)
    Write-Host "Switchin to another Window"
    switchWindow

    #enter password
    Write-Host "Entering School Password"
    # $emailSchoolPass = $driver.FindElementById("i0118")
    $emailSchoolPass = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("i0118") }
    $emailSchoolPass.SendKeys("...") #!! careful here

    #click next button to submit to login
    Write-Host "Clicking Next Button"
    # $enterNextButton = $driver.FindElementById("idSIButton9")
    $enterNextButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("idSIButton9") }
    $enterNextButton.Click()

    #click yes button
    Write-Host "delay with 2 seconds"
    Start-Sleep -Seconds 1
    Write-Host "Clicking 'Yes' Button"
    # $enterNextButton = $driver.FindElementById("idSIButton9")
    $enterNextButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("idSIButton9") }
    $enterNextButton.Click()

    Write-Host "you should be logged in to UC Canvas By Now!"

    Write-Host "delay with 2 seconds for upcoming boot site"
    Start-Sleep -Seconds 2

        
    # #we then login to github
    # loginToGithubUsingQuickie
}
function loginToClaudeAi {
    Write-Host "delay with 2 seconds for upcoming boot site"
    Start-Sleep -Seconds 2
    # # Make new window for my boy claude
    $driver.ExecuteScript("window.open();")

    switchWindow

    $driver.Navigate().GoToUrl("https://claude.ai/login");

    delay

    #loginCredentials
    # $emailClaudeField = $driver.FindElementById("email")
    $emailClaudeField = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("email") }
    $emailClaudeField.SendKeys("...") #!! careful here

    Write-Host "gmail for claude has been entered!"

    #click the continue with google button
    # $signInClaudeButton = $driver.FindElementByXPath("//div[contains(text(),'Continue with Google')]")
    $signInClaudeButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementByXPath("//div[contains(text(),'Continue with Google')]") }
    $signInClaudeButton.Click()


}
function loginToGithubUsingQuickie {
    # Open a new browser window
    $driver.ExecuteScript("window.open();")

    # Switch to the newly opened window
    switchWindow

    $driver.Navigate().GoToUrl("https://github.com/")
    #implement delay to wait for booting process
    delay
    # Click the "Sign in" button
    $signInButton = $driver.FindElementByClassName("d-inline-block")
    $signInButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementByClassName("d-inline-block") }
    $signInButton.Click()
    Write-Host "Sign-in Button Clicked"
    Write-Host "signinButton Clicked!"

    # Wait for the login field to be available
    Start-Sleep -Seconds 2

    #username and password for my github
    $loginField = $driver.FindElementById("login_field")
    $loginField = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("login_field") }
    $loginField.SendKeys("...") #!! careful here

    $passwordField = $driver.FindElementById("password")
    $passwordField = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementById("password") }
    $passwordField.SendKeys("...") #!! careful here

    Write-Host "Username and password successfully entered!"

    # Click the Sign-in button
    $signInButton = $driver.FindElementByClassName("btn-primary")
    $signInButton = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementByClassName("btn-primary") }
    $signInButton.Click()
    Write-Host "Sign-in Button Clicked"

    delay

    # Find the link by its data-test-selector attribute
    $link = $driver.FindElementByCssSelector("a[data-test-selector='gh-mobile-link']")
    $link = Wait-WebDriverElement -Driver $driver -ScriptBlock { $args[0].FindElementByCssSelector("a[data-test-selector='gh-mobile-link']") }

    # Click the link
    $link.Click()
    Write-Host "you should be logged in to your Github By Now!"

    Write-Host "delay with 2 seconds for upcoming boot site"
    Start-Sleep -Seconds 2
}


function loginNotionWithSeleniumBase() {
    python C:\Users\CJ\Desktop\LocalRepos\Quickie-Automation-Local\pow.scripts\QuickiePow\modules\quickieUC.py
}
 
#loginToUcCanvasUsingQuickie 

# # loginToClaudeAi #! work in progress
Start-Sleep -Seconds 2

loginToGithubUsingQuickie

Start-Sleep -Seconds 2
#loginNotionWithSeleniumBase
