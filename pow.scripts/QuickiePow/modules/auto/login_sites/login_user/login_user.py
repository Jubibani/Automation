import tkinter as tk
from tkinter import messagebox
import pandas as pd
import csv
import os

registered = False
global username, password

# Function to check if user is already registered
def is_user_registered(username, user_data_file_path):
    if not os.path.isfile(user_data_file_path):
        return False
    with open(user_data_file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == username:
                return True
    return False

# Function to store user data
def store_user_data(username, password, user_data_file_path):
    # Check if the file exists
    file_exists = os.path.isfile(user_data_file_path)

    # Open the file in append mode
    with open(user_data_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the header
        if not file_exists or os.stat(user_data_file_path).st_size == 0:
            writer.writerow(['Username', 'Password'])

        # Write the user data
        writer.writerow([username, password])

    print("User data stored successfully!")

user_data_file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\user.csv'
# Function to store site login data
def store_site_login_data(email, email_password, file_path):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Open the file in append mode  
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the header
        if not file_exists or os.stat(file_path).st_size == 0:
            writer.writerow(['email', 'email_password'])

        # Write the user data
        writer.writerow([email, email_password])

    print("Site login data stored successfully!")


file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv'

# store_site_login_data(email, email_password, file_path)
# Function to validate and register user to the site
def register_to_site():
    global entry_email, entry_email_password  # Declare as global to use these variables
    email = entry_email.get()
    email_password = entry_email_password.get()

    # Basic validation
    if not email or not email_password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        # Check if the email is already registered
        if is_user_registered(email, 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv'):
            messagebox.showinfo("Info", "Email already registered!")
        else:
            store_site_login_data(email, email_password, 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv')
            messagebox.showinfo("Success", "Site login credentials registered successfully!")
        entry_email.delete(0, tk.END)
        entry_email_password.delete(0, tk.END)

# Function to open email login window
def open_email_login_window():
    global entry_email, entry_email_password  # Declare as global to use these variables
    # Create main window for site registration
    email_login_window = tk.Toplevel(root)
    email_login_window.title("Email Login Form")

    # Create and place the labels and entry widgets for site registration
    label_UC_Canvas = tk.Label(email_login_window, text="UC email:")
    label_UC_Canvas.grid(row=0, column=0, padx=10, pady=5)
    entry_email = tk.Entry(email_login_window)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    label_UCpassword = tk.Label(email_login_window, text="Password:")
    label_UCpassword.grid(row=1, column=0, padx=10, pady=5)
    entry_email_password = tk.Entry(email_login_window, show="*")
    entry_email_password.grid(row=1, column=1, padx=10, pady=5)

    # Create and place the register button for site registration
    button_register_to_site = tk.Button(email_login_window, text="Register to UC", command=register_to_site)
    button_register_to_site.grid(row=3, columnspan=2, pady=10)

# Function to validate and register user
def register_user():
    username = entry_username.get()
    password = entry_password.get()

    # Basic validation
    if not username or not password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        store_user_data(username, password, 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\user.csv')
        messagebox.showinfo("Success", "User registered successfully!")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        open_email_login_window()

# Function to check user registration and proceed accordingly
def check_registration():
    username = entry_username.get()

    # Check if the user is already registered
    if is_user_registered(username, 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\user.csv'):
        messagebox.showinfo("Info", "User already registered. Proceeding to email login.")
        open_email_login_window()
    else:
        register_user()

# Create main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the labels and entry widgets
label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=5)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create and place the register button
button_register = tk.Button(root, text="Register", command=check_registration)
button_register.grid(row=3, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
