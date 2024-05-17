import  tkinter as tk
from tkinter import messagebox
import subprocess
import csv
import os

user_csv = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\user.csv'
#define funtions for registration and login for the user
def register_user(username, password):
    # Check if the file exists
    file_exists = os.path.isfile(user_csv)

    # Open the file in append mode
    with open(user_csv, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the header
        if not file_exists or os.stat(user_csv).st_size == 0:
            writer.writerow(['Username', 'Password'])

        # Write the user data
        writer.writerow([username, password])

    messagebox.showinfo("Success", "User registered successfully!")

def is_user_registered(username):
    try:
        with open(user_csv, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    return True
        return False
    except FileNotFoundError:
        return False

def check_user_credentials(username, password):
    try:
        with open(user_csv, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    return True
        return False
    except FileNotFoundError:
        return False


#define the tkinter gui
# Initialize main Tkinter window
root = tk.Tk()
root.title("Homepage")


#login functionalities
def find_quickiepass_and_run_script(filename):  #!! Canvas Log in
    # Iterate over all directories and subdirectories
    for root, dirs, files in os.walk("C:\\Quickie-Automation"):
        # Check if the target file is found in the current directory
        if filename in files:
            # Construct the full path to the script
            script_path = os.path.join(root, filename)
            # Run the PowerShell script
            subprocess.Popen(["powershell.exe", "-File", script_path])

# Call the function to find and run the target script
# find_quickie_canvas_and_run_script("quickie_canvas.ps1")
# Function to open login form# Function to open the login form
def open_login_form():
    login_window = tk.Toplevel(root)
    login_window.title("Login Form")

    tk.Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    entry_email = tk.Entry(login_window)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(login_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    def login():
        username = entry_email.get()
        password = entry_password.get()
        if check_user_credentials(username, password):
            messagebox.showinfo("Success", "Login successful!")
            find_quickiepass_and_run_script("quickiePass.ps1")
            login_window.destroy()  # Close login window
        else:
            messagebox.showerror("Error", "Invalid email or password!")
            #open register form

    tk.Button(login_window, text="Login", command=login).grid(row=2, columnspan=2, pady=10)

# Function to open registration form
def open_registration_form():
    registration_window = tk.Toplevel(root)
    registration_window.title("Registration Form")

    tk.Label(registration_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(registration_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(registration_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    def register():
        username = entry_username.get()
        password = entry_password.get()
        if is_user_registered(username):
            messagebox.showinfo("Info", "Email already registered!")
        else:
            register_user(username, password)
            registration_window.destroy()  # Close registration window

    tk.Button(registration_window, text="Register", command=register).grid(row=2, columnspan=2, pady=10)

# Main homepage buttons
tk.Button(root, text="Login", command=open_login_form).pack(pady=10)
tk.Button(root, text="Register", command=open_registration_form).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
