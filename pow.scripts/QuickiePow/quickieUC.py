from seleniumbase import BaseCase   
from seleniumbase import Driver
import traceback

BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")

class UndetectedLoginTest(BaseCase):
    def loging_test_undetected(self):
        for _ in range(5):  # Retry the test up to 3 times
            try:
                driver = Driver(uc=True)
                url = "https://www.notion.so/login"
                driver.uc_open_with_reconnect(url, 3)
                driver.sleep(2)
                
                # Your login steps here
                driver.wait_for_element('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
                driver.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
                driver.sleep(2)

                window_handles = driver.window_handles
                print("Window Handles:", window_handles)
                driver.switch_to.window(window_handles[1])

                driver.sleep(2)
                driver.type("//input[@id='identifierId']", "...")
                driver.sleep(2)
                driver.click("#identifierNext")
                driver.sleep(2)

                driver.wait_for_element_visible("[aria-label='Enter your password']")
                driver.type("[aria-label='Enter your password']", "...")
                driver.sleep(2)
                driver.click("#passwordNext")

                print("You should be logged in to your Notion By Now!") 

                while True:
                    print("successfully loaded notion")
                    pass #TODO: refactor code where the code completely stops after driver stops
                        #!! bug: program still runs despite being exited
                break  # If the test runs successfully, exit the loop

            except Exception as e:
                print("An error occurred:", e)
                traceback.print_exc()  # Print the traceback for debugging
                print("Retrying...")
                driver.quit()  # Quit the driver before retrying

if __name__ == "__main__":
    UndetectedLoginTest().loging_test_undetected()
