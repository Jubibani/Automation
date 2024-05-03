from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

chromeDriverPath = "C:\\selenium-selenium-4.18.0\\chromedriver.exe"
service = Service(chromeDriverPath)

def loginToNotionUsingQuickie():
    # Create ChromeOptions instance for the new window
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    # Create a new ChromeDriver instance with ChromeOptions for the new window
    newDriver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the website where you want to log in (in the new window)
    newDriver.get("https://www.notion.so/login")
    print("Proceeded to notion")

    # Wait for the page to load
    time.sleep(2)

    # Click for the Gmail button
    continueWithGmailButton = newDriver.find_element(By.XPATH, "//*[@id='notion-app']/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div")
    print("Continuing with Gmail Account")
    continueWithGmailButton.click()

    print("Button Clicked")
    time.sleep(2)

    # Switch to the new window
    newDriver.switch_to.window(newDriver.window_handles[-1])

    # Find the email input field and enter the Gmail address
    emailInputField = WebDriverWait(newDriver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
    )
    print("Email Input has been Identified")
    emailInputField.send_keys("...")
    print("Gmail successfully entered")

    time.sleep(2)

    # Find the div wrapping the button by its id
    nextDiv = newDriver.find_element(By.ID, "identifierNext")

    # Click the div
    nextDiv.click()

    print("JsController clicked!")
    print("You should be logged in to your Notion By Now!")
    time.sleep(2)

loginToNotionUsingQuickie()