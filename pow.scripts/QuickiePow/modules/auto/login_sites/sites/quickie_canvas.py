# Import necessary components
from seleniumbase import BaseCase
from seleniumbase import Driver
import time
import base64
import pandas as pd
from cryptography.fernet import Fernet
import os

# Define the path to the key file
key_file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\secret.key'
file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv'

# Ensure the key file exists at the specified path
if not os.path.exists(key_file_path):
    raise FileNotFoundError(f"No such file or directory: '{key_file_path}'")

# Load the encryption key
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')

def get_canvas_credentials(file_path):
    try:
        df = pd.read_csv(file_path)
        print("DataFrame Contents:", df)  # Debugging statement
        if not df.empty:
            email_encrypted_base64 = df.iloc[-1]['email']
            password_encrypted_base64 = df.iloc[-1]['email_password']
            
            # Decode Base64-encoded strings
            email_encrypted = base64.b64decode(email_encrypted_base64)
            password_encrypted = base64.b64decode(password_encrypted_base64)
            
            # Decrypt the binary data
            email = decrypt_data(email_encrypted)
            password = decrypt_data(password_encrypted)
            
            print("Found credentials: Email:", email, "Password:", password)  # Debugging statement
            return email, password
        else:
            print("No credentials found in the CSV file.")  # Debugging statement
            return None, None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")  # Debugging statement
        return None, None

class UndetectedCanvasLogin(BaseCase):
    def login_to_canvas(self):
        # Navigate to school Canvas
        url = "https://uc-bcf.instructure.com/"
        print("Opening URL:", url)
        driver.uc_open_with_reconnect(url, 3)

        # Implement delay to wait for the booting process
        time.sleep(5)  # Adjust this delay as needed

        # Get QuickieCanvas credentials
        email, email_password = get_canvas_credentials(file_path)
        print("Decrypted email: ", email)
        print("Decrypted email password: ", email_password)
        
        # Debugging the email
        if email is None:
            print("Email is None!")  # Debugging statement
            return
        else:
            print("Email:", email)  # Debugging statement
        
        # Enter school email for Canvas login
        print("Waiting for email input element")
        driver.wait_for_element("#i0116", timeout=20)
        print("Found email input element")
        driver.type("#i0116", email)
        print("Entered email:", email)

        # Click Next button after entering the email
        print("Waiting for next button after email input")
        driver.wait_for_element("#idSIButton9", timeout=20)
        print("Found next button after email input")
        driver.click("#idSIButton9")
        print("Clicked next button after email input")

        time.sleep(5)  # Adjust this delay as needed

        # Enter password
        print("Waiting for password input element")
        driver.wait_for_element("#i0118", timeout=20)
        print("Found password input element")
        driver.type("#i0118", email_password)
        print("Entered password")

        # Click Next button to submit login
        print("Waiting for next button after password input")
        driver.wait_for_element("#idSIButton9", timeout=20)
        print("Found next button after password input")
        driver.click("#idSIButton9")
        print("Clicked next button after password input")

        # Click Yes button (if needed)
        print("Waiting for Yes button")
        driver.wait_for_element("#idSIButton9", timeout=20)
        print("Found Yes button")
        driver.click("#idSIButton9")
        print("Clicked Yes button")

        print("You should be logged in to UC Canvas by now!") 

        try:
            # Infinite loop to keep the browser open
            while True:
                time.sleep(1)  # Keep the browser open
        except Exception as e:
            print(f"An error occurred: {e}")
            driver.quit()

if __name__ == "__main__":
    driver = Driver(uc=True)  # this enables the uc mode
    UndetectedCanvasLogin().login_to_canvas()
