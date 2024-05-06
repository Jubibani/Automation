from seleniumbase import BaseCase


class NotionLoginTest(BaseCase):
    def test_login_to_notion(self):
        self.open("https://www.notion.so/login")
        self.assert_element("#notion-app")  # Verify that the page is loaded

        # Click for the Gmail button
        self.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        self.wait_for_element_visible("//input[@id='identifierId']").send_keys("strawberryloli3@gmail.com")
        self.click('//*[@id="identifierNext"]')

        # Wait for the login page to load
        self.assert_element("#identifierId")

        # Perform other actions as needed

        # Wait for Notion to load and verify successful login
        self.wait_for_element_visible("//div\[@class='notion-app'\]")
        self.assert_text("Notion", "div.notion-topbar")

if __name__ == "__main__":
    # Run the test case
    BaseCase.main(__name__, __file__)
