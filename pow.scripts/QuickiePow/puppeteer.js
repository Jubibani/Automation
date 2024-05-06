const puppeteer = require('puppeteer');

async function loginToNotionUsingQuickie() {
    // Launch a new browser instance
    const browser = await puppeteer.launch();

    // Create a new page within the browser
    const page = await browser.newPage();

    // Navigate to the Notion login page
    await page.goto('https://www.notion.so/login');
    console.log("Proceeded to Notion");

    // Add a delay (You may need to implement your own delay function)
    await delay();

    // Click on the "Continue with Gmail" button
    await page.click('#notion-app div div:nth-child(1) div main div:nth-child(1) section div div div div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1) div');
    console.log("Continuing with Gmail Account");

    // Add a delay
    await delay();

    // Switch to the new window
    const pages = await browser.pages();
    await page.bringToFront();

    // Find the email input field and enter the Gmail address
    const emailInputField = await page.waitForXPath("//input[@id='identifierId']");
    console.log("Email Input has been Identified");
    await emailInputField.type("strawberryloli3@gmail.com");
    console.log("Gmail successfully entered");

    // Find the "Next" button and click it
    const nextButton = await page.$("#identifierNext");
    await nextButton.click();
    console.log("JsController clicked!");

    console.log("You should be logged in to your Notion By Now!");

    // Close the browser after 2 seconds delay
    await delay(2000);
    await browser.close();
}

// Function to implement delay
async function delay(ms = 1000) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

loginToNotionUsingQuickie();
