#import necessarry components
from seleniumbase import BaseCase
from seleniumbase import Driver
import time

#making the driver global
#? why: Because this is an independent script and is only to be integrated to a main script.
driver = Driver(uc=True) #this enables the uc mode

BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")

class UndetectedCanvasLogin(BaseCase):
    def login_to_canvas(self):
    #navigate to school Canvas
        url = "https://uc-bcf.instructure.com/"
        driver.uc_open_with_reconnect(url, 3)

        # Implement delay to wait for booting process
        time.sleep(3)  # Adjust this delay as needed

        # Enter school email for Canvas login
        driver.wait_for_element("#i0116")

        driver.type("#i0116", "cao5224@students.uc-bcf.edu.ph")  # Replace selector with the appropriate one

        driver.type("#i0116", "...")  # Replace selector with the appropriate one


        # Click Next button after entering the email
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")  # Replace selector with the appropriate one

        time.sleep(3)  # Adjust this delay as needed

        # Enter password
        driver.wait_for_element("#i0118")
        driver.type("#i0118", "...")  # Replace selector with the appropriate one

        # Click Next button to submit login
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")  # Replace selector with the appropriate one

        # Click Yes button (if needed)
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")  # Replace selector with the appropriate one

        print("You should be logged in to UC Canvas By Now!") 

if __name__ == "__main__":
    UndetectedCanvasLogin().login_to_canvas()
