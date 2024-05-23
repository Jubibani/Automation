import tkinter as tk
from tkinter import messagebox
import subprocess
import csv
import os
import bcrypt
import base64
from cryptography.fernet import Fernet


user_csv = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\user.csv'
file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\login_for_sites.csv'
tempfile = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\modules\\auto\\login_sites\\login_user\\login_for_sites\\temp\\tempfile.csv'
# Define the path to the key file
key_file_path = 'C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\secret.key'

# Generate or load the encryption key
if not os.path.exists(key_file_path):
    # If the key file doesn't exist, generate a new key and save it
    key = Fernet.generate_key()
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)
else:
    # If the key file exists, load the key from it
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()
    
# Initialize a Fernet cipher object with the key
cipher_suite = Fernet(key)

# Function to hash a password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

# Function to check if a password matches a hashed password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def register_user(username, password):
    # Check if the file exists
    file_exists = os.path.isfile(user_csv)

    # Hash the password
    hashed_password = hash_password(password)

    # Open the file in append mode
    with open(user_csv, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the header
        if not file_exists or os.stat(user_csv).st_size == 0:
            writer.writerow(['Username', 'Password'])

        # Write the user data
        writer.writerow([username, hashed_password.decode('utf-8')])

    messagebox.showinfo("Success", "User registered successfully!")

def is_user_registered(username, file=user_csv):
    try:
        with open(file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    return True
        return False
    except FileNotFoundError:
        return False

def is_any_user_registered():
    try:
        with open(user_csv, mode='r') as file:
            reader = csv.DictReader(file)
            for _ in reader:
                return True
        return False
    except FileNotFoundError:
        return False

def check_user_credentials(username, password):
    try:
        with open(user_csv, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username:
                    if check_password(password, row['Password']):
                        return True
        return False
    except FileNotFoundError:
        return False

# def store_site_login_data(email, email_password, file_path): ##!Hashed Version
#     # Check if the file exists
#     file_exists = os.path.isfile(file_path)

#     # Hash the email password
#     hashed_email_password = hash_password(email_password)

#     # Open the file in append mode
#     with open(file_path, mode='a', newline='') as file:
#         writer = csv.writer(file)

#         # If the file does not exist or is empty, write the header
#         if not file_exists or os.stat(file_path).st_size == 0:
#             writer.writerow(['email', 'email_password'])

#         # Write the user data
#         writer.writerow([email, hashed_email_password.decode('utf-8')])

#     print("Site login data stored successfully!")
##! Using cryptogrpahy
# # Generate a random encryption key (only once)
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

def store_site_login_data(email, email_password, file_path):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    # Encrypt the email and email password
    email_encrypted = cipher_suite.encrypt(email.encode('utf-8'))
    password_encrypted = cipher_suite.encrypt(email_password.encode('utf-8'))

    # Encode the encrypted data as Base64
    email_encrypted_base64 = base64.b64encode(email_encrypted).decode('utf-8')
    password_encrypted_base64 = base64.b64encode(password_encrypted).decode('utf-8')

    # Open the file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # If the file does not exist or is empty, write the header
        if not file_exists or os.stat(file_path).st_size == 0:
            writer.writerow(['email', 'email_password'])

        # Write the encrypted user data
        writer.writerow([email_encrypted_base64, password_encrypted_base64])

    print("Site login data stored successfully!")

def register_to_site():
    global entry_email, entry_email_password, email_login_window  # Declare as global to use these variables
    email = entry_email.get()
    email_password = entry_email_password.get()

    # Basic validation
    if not email or not email_password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        # Check if the email is already registered
        if is_user_registered(email, file_path):
            messagebox.showinfo("Info", "Email already registered!")
        else:
            store_site_login_data(email, email_password, file_path)
            messagebox.showinfo("Success", "Site login credentials registered successfully!")
            email_login_window.destroy()
        entry_email.delete(0, tk.END)
        entry_email_password.delete(0, tk.END)

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
            find_quickielog_and_run_script("quickieLog.py")
            login_window.destroy()  # Close login window
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    tk.Button(login_window, text="Login", command=login).grid(row=2, columnspan=2, pady=10)

def open_registration_form():
    if is_any_user_registered():
        messagebox.showinfo("Existing User Found", "Currently, the program can only accept one local user.")
        return

    registration_window = tk.Toplevel(root)
    registration_window.title("Registration Form")

    tk.Label(registration_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    entry_username = tk.Entry(registration_window)
    entry_username.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(registration_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(registration_window, text="Login details will be saved locally.").grid(row=2, columnspan=2, pady=10)

    def register():
        username = entry_username.get()
        password = entry_password.get()
        if is_user_registered(username):
            messagebox.showinfo("Existing User Found", "Currently, the program can only accept one local user.")
        else:
            register_user(username, password)
            open_email_login_window()
            registration_window.destroy()  # Close registration window

    tk.Button(registration_window, text="Register", command=register).grid(row=3, columnspan=2, pady=10)

def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    tk.Label(about_window, text="Quickie Automation is a program developed by Jubibani that is programmed to automate the login to your sites (currently: UC canvas) with the credentials that is saved locally.").pack(padx=20, pady=20)
    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=10)

def open_email_login_window():
    global entry_email, entry_email_password, email_login_window  # Declare as global to use these variables
    email_login_window = tk.Toplevel(root)
    email_login_window.title("Email Login Form")

    tk.Label(email_login_window, text="UC email:").grid(row=0, column=0, padx=10, pady=5)
    entry_email = tk.Entry(email_login_window)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(email_login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    entry_email_password = tk.Entry(email_login_window, show="*")
    entry_email_password.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(email_login_window, text="Register to UC", command=register_to_site).grid(row=3, columnspan=2, pady=10)

def open_registration_and_email_login():
    open_registration_form()

def find_quickielog_and_run_script(filename):  #!! Login Bridge
    for root_dir, dirs, files in os.walk("C:\\Quickie-Automation"):
        if filename in files:
            script_path = os.path.join(root_dir, filename)
            subprocess.Popen(["python", script_path])

root = tk.Tk()
root.title("Homepage")
root.iconbitmap("C:\\Quickie-Automation\\pow.scripts\\QuickiePow\\logo\\logoAppIco.ico")
root.geometry("800x600")  # Set the window size

center_frame = tk.Frame(root)
center_frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Button(center_frame, text="Login", command=open_login_form).pack(pady=10)
tk.Button(center_frame, text="Register", command=open_registration_and_email_login).pack(pady=10)
tk.Button(center_frame, text="About", command=open_about_window).pack(pady=10)

root.mainloop()
