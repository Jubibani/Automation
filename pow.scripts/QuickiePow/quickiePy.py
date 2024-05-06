from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--uc", "-s")


class NotionLoginTest(BaseCase):
    def test_login_to_notion(self):
        url = "https://www.notion.so/login"
        if not self.undetectable:
            self.get_new_driver(undetectable=True)
        self.driver.uc_open_with_reconnect(url, 3)
        self.wait(2)

        # ... your login steps here ...
        self.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        self.wait(2)

        # Switch to the new window
        self.switch_to_window(1)

        # Find the email input field and enter the Gmail address
        self.type("//input[@id='identifierId']", "...")
        self.wait(2)

        # Click the "Next" button
        self.click("#identifierNext")
        self.wait(2)

        print("You should be logged in to your Notion By Now!")

if __name__ == "__main__":
    NotionLoginTest().test_login_to_notion()