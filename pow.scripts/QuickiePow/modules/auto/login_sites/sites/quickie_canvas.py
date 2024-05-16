# Import necessary components
from seleniumbase import BaseCase
from seleniumbase import Driver
import pandas as pd
import time

# Function to get login credentials from CSV
def get_canvas_credentials(file_path):
    try:
        df = pd.read_csv(file_path)
        if not df.empty:
            email = df.iloc[-1]['email']  # Retrieve the last registered email
            password = df.iloc[-1]['email_password']  # Retrieve the password corresponding to the last registered email
            print("Found credentials: Email:", email, "Password:", password)  # Debugging statement
            return email, password
        else:
            print("No credentials found in the CSV file.")  # Debugging statement
            return None, None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None, None

# Making the driver global
driver = Driver(uc=True)  # this enables the uc mode

BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")

class UndetectedCanvasLogin(BaseCase):
    def login_to_canvas(self):
        # navigate to school Canvas
        url = "https://uc-bcf.instructure.com/"
        driver.uc_open_with_reconnect(url, 3)

        # Implement delay to wait for booting process
        time.sleep(3)  # Adjust this delay as needed

        # Get QuickieCanvas credentials
        email, email_password = get_canvas_credentials('C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv')

        # Debugging the email
        if email is None:
            print("Email is None!")  # Debugging statement
        else:
            print("Email:", email)  # Debugging statement
        
        # Enter school email for Canvas login
        driver.wait_for_element("#i0116")
        driver.type("#i0116", email)

        # Click Next button after entering the email
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")

        time.sleep(3)  # Adjust this delay as needed

        # Enter password
        driver.wait_for_element("#i0118")
        driver.type("#i0118", email_password)

        # Click Next button to submit login
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")

        # Click Yes button (if needed)
        driver.wait_for_element("#idSIButton9")
        driver.click("#idSIButton9")

        print("You should be logged in to UC Canvas By Now!") 

if __name__ == "__main__":
    UndetectedCanvasLogin().login_to_canvas()
