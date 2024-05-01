# Import Selenium WebDriver module
Import-Module Selenium

# Set the path to GeckoDriver executable
$geckoDriverPath = "C:\geckodriver-v0.34.0-win64\geckodriver.exe"

# Add the directory containing Selenium WebDriver DLLs to the assembly path
$assemblyPath = "C:\selenium-selenium-4.18.0"
$null = [System.Reflection.Assembly]::LoadFrom("$assemblyPath\WebDriver.dll")
$null = [System.Reflection.Assembly]::LoadFrom("$assemblyPath\Selenium.Firefox.WebDriver.dll")

# Create FirefoxOptions instance
$firefoxOptions = New-Object OpenQA.Selenium.Firefox.FirefoxOptions

# Create a new FirefoxDriver instance with FirefoxOptions
$driver = New-Object OpenQA.Selenium.Firefox.FirefoxDriver($geckoDriverPath, $firefoxOptions)

# Navigate to a webpage
$driver.Navigate().GoToUrl("https://www.notion.so/login")
d# Rest of your Selenium automation code goes here
