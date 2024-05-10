from seleniumbase import BaseCase   
from seleniumbase import Driver
import time
import subprocess
import traceback
import tkinter as tk
import threading

#making it global
driver = Driver(uc=True)
# Define the pop-up GUI functions
def show_error_popup(error_message):
    def run_sub_process_python_script():
        subprocess.run(["python", "C:\\Users\\CJ\\Desktop\\LocalRepos\\Quickie-Automation-Local\\pow.scripts\\QuickiePow\\modules\\quickieUC.py"])

    def retry_action():
        print("retry phase")
        threading.Thread(target=run_sub_process_python_script).start()
        time.sleep(2)
        popup.destroy()

    def quit_action():
        driver.quit()
        time.sleep(2)
        popup.destroy()

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
        driver.quit()
        time.sleep(2)
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
        time.sleep(2)
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

# def show_countdown_popup(duration):
#     popup = tk.Tk()
#     popup.geometry("300x200")
#     popup.title("Countdown")
#     label = tk.Label(popup, text="Countdown:")
#     label.pack(pady=10)
#     countdown_label = tk.Label(popup, text=duration)
#     countdown_label.pack(pady=10)

#     def update_countdown():
#         nonlocal duration
#         while duration > 0:
#             countdown_label.config(text=str(duration))
#             time.sleep(1)
#             duration -= 1
#         popup.destroy()

#     threading.Thread(target=update_countdown).start()
#     popup.mainloop()
BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")


class UndetectedLoginTest(BaseCase):
    def loging_test_undetected(self):
        message = "do you want to run notion?"
        show_pop_up_notion_running(message)
        # error_message = "sometimes, notion is flaky. but i'm here. let me know if you want to restart. if notion sucessfully logged in. feel free to close this window."

        # threading.Thread(target=show_error_popup, args=(error_message,)).start()
        # # show_error_popup(error_message)


        driver = Driver(uc=True) #!this is needed
        url = "https://www.notion.so/login"
        driver.uc_open_with_reconnect(url, 3)
        
        # Your login steps here
        driver.wait_for_element('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')
        driver.click('//*[@id="notion-app"]/div/div[1]/div/main/div[1]/section/div/div/div/div[2]/div[1]/div[1]/div[1]/div')

        window_handles = driver.window_handles
        print("Window Handles:", window_handles)
        driver.switch_to.window(window_handles[1])

        driver.wait_for_element("//input[@id='identifierId']")
        driver.type("//input[@id='identifierId']", "...")
        
        driver.wait_for_element("#identifierNext")
        driver.click("#identifierNext")

        driver.wait_for_element_visible("[aria-label='Enter your password']")
        driver.type("[aria-label='Enter your password']", "...")

        driver.wait_for_element("#passwordNext")
        driver.click("#passwordNext")

        print("You should be logged in to your Notion By Now!") 
        while True:
            print("successfully loaded notion")

            pass #TODO: refactor code where the code completely stops after driver stops
                #!!bug: sometimes, program still runs despite being exited               

if __name__ == "__main__":
    try:
        UndetectedLoginTest().loging_test_undetected()
    except Exception as e: 
        # print("An error occurred:", e)
        # traceback.print_exc()  # Print the traceback for debugging
        # print("Retrying...")
        print("rebooting phase")
        error_message = "Would You Like to Retry?"
        show_error_popup(error_message)
