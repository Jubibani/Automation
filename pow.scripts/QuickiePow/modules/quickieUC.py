from seleniumbase import BaseCase   
from seleniumbase import Driver
import time
import traceback
import tkinter as tk
import threading
# Define the pop-up GUI functions
def show_error_popup(error_message):
    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("Error")
    label = tk.Label(popup, text=error_message)
    label.pack(pady=10)
    popup.mainloop()

def show_pop_up_notion_running(_message):
    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("message")
    label = tk.Label(popup, text=_message)
    label.pack(pady=10)
    popup.mainloop()


def show_countdown_popup(duration):
    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("Countdown")
    label = tk.Label(popup, text="Countdown:")
    label.pack(pady=10)
    countdown_label = tk.Label(popup, text=duration)
    countdown_label.pack(pady=10)

    def update_countdown():
        nonlocal duration
        while duration > 0:
            countdown_label.config(text=str(duration))
            time.sleep(1)
            duration -= 1
        popup.destroy()

    threading.Thread(target=update_countdown).start()
    popup.mainloop()
BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")

class UndetectedLoginTest(BaseCase):
    # def loging_test_undetected_with_retry(self):
    #     for _ in range(5):  # Retry the test up to 3 times
    #         try:
                
    #             driver = Driver(uc=True)
    #             url = "https://www.notion.so/login"
    #             driver.uc_open_with_reconnect(url, 3)
    #             show_pop_up_notion_running("Notion is now running")
    #             driver.sleep(2)
                
    #             # Your login steps here
    #             driver.wait_for_element('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
    #             driver.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
    #             driver.sleep(2)

    #             window_handles = driver.window_handles
    #             print("Window Handles:", window_handles)
    #             driver.switch_to.window(window_handles[1])

    #             driver.sleep(2)
    #             driver.type("//input[@id='identifierId']", "...")
    #             driver.sleep(2)
    #             driver.click("#identifierNext")
    #             driver.sleep(2)

    #             driver.wait_for_element_visible("[aria-label='Enter your password']")
    #             driver.type("[aria-label='Enter your password']", "...")
    #             driver.sleep(2)
    #             driver.click("#passwordNext")

    #             print("You should be logged in to your Notion By Now!") 

    #             while True:
    #                 print("successfully loaded notion")

    #                 pass #TODO: refactor code where the code completely stops after driver stops
    #                     #!! bug: program still runs despite being exited               
    #             break  # If the test runs successfully, exit the loop
    #         except Exception as e:
    #             print("An error occurred:", e)
    #             traceback.print_exc()  # Print the traceback for debugging
    #             print("Retrying...")
    #             # Display error popup
    #             show_error_popup("An error occurred:\n" + traceback.format_exc() + "\nRetrying...")


        def loging_test_undetected(self):
            driver = Driver(uc=True)
            url = "https://www.notion.so/login"
            driver.uc_open_with_reconnect(url, 3)
            # show_pop_up_notion_running("Notion is now running")
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

            # while True:
            #     print("successfully loaded notion")
            #     pass #TODO: refactor code where the code completely stops after driver stops
            #         #!! bug: program still runs despite being exited               
            #     if driver.quit(): 
            #         break# If the test runs successfully, exit the loop

if __name__ == "__main__":
    UndetectedLoginTest().loging_test_undetected()
