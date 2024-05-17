import os
import subprocess
import time

def find_quickie_canvas_and_run_script(filename): #!! Canvas Log in
    # Iterate over all directories and subdirectories
    for root, dirs, files in os.walk("C:\Quickie-Automation"):
        # Check if the target file is found in the current directory
        if filename in files:
            # Construct the full path to the script
            script_path = os.path.join(root, filename)
            # Run the script as a separate process
            subprocess.Popen(["python", script_path])

# Call the function to find and run the target script
find_quickie_canvas_and_run_script("quickie_canvas.py")

time.sleep(3)

# def find_quickie_github_and_run_script(filename): #!! Github Log in
#     # Iterate over all directories and subdirectories
#     for root, dirs, files in os.walk("C:\Quickie-Automation"):
#         # Check if the target file is found in the current directory
#         if filename in files:
#             # Construct the full path to the script
#             script_path = os.path.join(root, filename)
#             # Run the script as a separate process
#             subprocess.Popen(["python", script_path])

# # Call the function to find and run the target script
# find_quickie_github_and_run_script("quickie_github.py")

# def find_quickie_notion_and_run_script(filename): #!! Notion Log in
#     # Iterate over all directories and subdirectories
#     for root, dirs, files in os.walk("C:\Quickie-Automation"):
#         # Check if the target file is found in the current directory
#         if filename in files:
#             # Construct the full path to the script
#             script_path = os.path.join(root, filename)
#             # Run the script as a separate process
#             subprocess.Popen(["python", script_path])

# # Call the function to find and run the target script
# find_quickie_notion_and_run_script("quickie_notion.py")
