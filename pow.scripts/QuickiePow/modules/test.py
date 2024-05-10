from seleniumbase import BaseCase   
from seleniumbase import Driver
import time
import traceback
import tkinter as tk
import threading

#making it global
driver = Driver(uc=True)
# Define the pop-up GUI functions
def show_error_popup(error_message):
    def retry_action():
        UndetectedLoginTest().loging_test_undetected()
        popup.destroy()
        # Perform retry action here

    def quit_action():
        driver.quit()
        popup.destroy()
        # Perform quit action here

    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("Error, Notion Boot up Failed")

    label = tk.Label(popup, text=error_message)
    label.pack(pady=10)

    retry_button = tk.Button(popup, text="Retry", command=retry_action)
    retry_button.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(popup, text="Quit", command=quit_action)
    quit_button.pack(side=tk.RIGHT, padx=5)

    popup.mainloop()

def show_pop_up_notion_running(message):
    def yes_action():
        # Action to take if user selects Yes
        popup.destroy()
        # Perform your action here when the user selects Yes

    def no_action():
        # Action to take if user selects No
        popup.destroy()
        # Perform your action here when the user selects No

    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("Message")

    label = tk.Label(popup, text=message)
    label.pack(pady=10)

    yes_button = tk.Button(popup, text="Yes", command=yes_action)
    yes_button.pack(side=tk.LEFT, padx=5)

    no_button = tk.Button(popup, text="No", command=no_action)
    no_button.pack(side=tk.RIGHT, padx=5)

    popup.mainloop()

def show_pop_up_to_break_notion(break_message):
    def yes_action():
        # Action to take if user selects Yes
        driver.quit()
        print("driver has quit the script")
        popup.destroy()
        # Perform your action here when the user selects Yes

    def no_action():
        # Action to take if user selects No
        popup.destroy()
        # Perform your action here when the user selects No

    popup = tk.Tk()
    popup.geometry("300x200")
    popup.title("Message")

    label = tk.Label(popup, text=break_message)
    label.pack(pady=10)

    yes_button = tk.Button(popup, text="Yes", command=yes_action)
    yes_button.pack(side=tk.LEFT, padx=5)

    no_button = tk.Button(popup, text="No", command=no_action)
    no_button.pack(side=tk.RIGHT, padx=5)

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
    #             driver.type("//input[@id='identifierId']", "strawberryloli3@gmail.com")
    #             driver.sleep(2)
    #             driver.click("#identifierNext")
    #             driver.sleep(2)

    #             driver.wait_for_element_visible("[aria-label='Enter your password']")
    #             driver.type("[aria-label='Enter your password']", "Jubibi'sstrawbibi")
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
        # for _ in range(5):  # Retry the test up to 5 times
        #     try:
            #? user prompt
            message = "do you want to run notion?"
            show_pop_up_notion_running(message)
            # driver = Driver(uc=True)
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
            driver.type("//input[@id='identifierId']", "strawberryloli3@gmail.com")
            driver.sleep(2)
            driver.click("#identifierNext")
            driver.sleep(2)

            driver.wait_for_element_visible("[aria-label='Enter your password']")
            driver.type("[aria-label='Enter your password']", "Jubibi'sstrawbibi")
            driver.sleep(2)
            driver.click("#passwordNext")

            print("You should be logged in to your Notion By Now!") 

            # while True:
            #     print("successfully loaded notion")        
            #     time.sleep(1)      
            #     if driver.quit(): 
            #         break_message = "would you like to quit the driver?"
            #         show_pop_up_to_break_notion(break_message)
            #         break# If the test runs successfully, exit the loop
            #     else:pass
                
            while True:
                print("successfully loaded notion")

                pass #TODO: refactor code where the code completely stops after driver stops
                    #!!bug: sometimes, program still runs despite being exited               
            
            # # Display error popup
            # except Exception as e:
            #     print("An error occurred:", e)
            #     traceback.print_exc()  # Print the traceback for debugging
            #     print("Retrying...")
            #     # Display error popup
            #     show_error_popup("An error occurred:\n" + traceback.format_exc() + "\nRetrying...")
            #     error_message = "Would You Like to Retry?"
            #     show_error_popup(error_message)
if __name__ == "__main__":
    try:
        UndetectedLoginTest().loging_test_undetected()
    except Exception as e: 
        print("An error occurred:", e)
        traceback.print_exc()  # Print the traceback for debugging
        print("Retrying...")
        # Display error popup
        show_error_popup("An error occurred:\n" + traceback.format_exc() + "\nRetrying...")
    finally:
        print("rebooting phase")
        error_message = "Would You Like to Retry?"
        show_error_popup(error_message)