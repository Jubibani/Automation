from seleniumbase import BaseCase   
from seleniumbase import Driver


BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")

class UndetectedLoginTest(BaseCase):
    def loging_test_undetected(self):
        driver = Driver(uc=True)
        url = "https://www.notion.so/login"
        # if not driver.undetectable: #!! needs to be refactored
        #     driver.get_new_driver(undetectable=True)
        driver.uc_open_with_reconnect(url, 3)
        driver.sleep(2)
        
        # Your login steps here
        driver.wait_for_element('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        driver.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        driver.sleep(2)

                # Get a list of all window handles
        window_handles = driver.window_handles

        # Print all window handles
        print("Window Handles:", window_handles)

        # Switch to the second window (index 1)
        driver.switch_to.window(window_handles[1])


        driver.sleep(2)
        # driver.switch_to_window()
        driver.type("//input[@id='identifierId']", "...")
        driver.sleep(2)
        driver.click("#identifierNext")
        driver.sleep(2)

        #Enter Password
        driver.wait_for_element_visible("[aria-label='Enter your password']")
        driver.type("[aria-label='Enter your password']", "...")

        driver.sleep(2)
        driver.click("#passwordNext")


        print("You should be logged in to your Notion By Now!") 

        while True:
            print("sucessfully loaded notion")
            pass #!! do nothing

if __name__ == "__main__":
    UndetectedLoginTest().loging_test_undetected()
