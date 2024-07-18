from tkinter import *
from tkinter import messagebox
import random
import string

# Function to check password strength
def check_password_strength(password):
    strength = 0
    
    # Check length
    if len(password) >= 8:
        strength += 1
    
    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    
    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    
    # Check for special characters
    special_chars = set(string.punctuation)
    if any(char in special_chars for char in password):
        strength += 1
    
    return strength

# Function to generate a strong password
def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Function to handle password checking and generation
def process_password():
    password = password_var.get()
    
    if len(password) == 0:
        messagebox.showerror("Error", "Please enter a password.")
        return
    
    strength = check_password_strength(password)
    
    if strength == 5:
        strength_label.config(text="Very Strong", fg="green")
    elif strength >= 3:
        strength_label.config(text="Strong", fg="blue")
    elif strength >= 2:
        strength_label.config(text="Moderate", fg="orange")
    else:
        strength_label.config(text="Weak", fg="red")
    
    password_entry.delete(0, END)

# Main window setup
window = Tk()
window.title("Password Strength Checker & Generator")
window.geometry("400x300")
window.configure(bg="#ffffff")

# Title label
title_label = Label(window, text="Password Strength Checker & Generator", font=("Helvetica", 18, "bold"), bg="#ffffff")
title_label.pack(pady=10)

# Frame for input fields
frame = Frame(window, bg="#ffffff")
frame.pack(pady=10)

# Password entry
password_label = Label(frame, text="Enter Password:", font=("Helvetica", 12), bg="#ffffff")
password_label.grid(row=0, column=0, padx=10, pady=5)
password_var = StringVar()
password_entry = Entry(frame, textvariable=password_var, font=("Helvetica", 12), show="*")
password_entry.grid(row=0, column=1, padx=10, pady=5)

# Check button
check_button = Button(window, text="Check Strength", font=("Helvetica", 14), command=process_password, bg="#4CAF50", fg="#ffffff")
check_button.pack(pady=10)

# Strength label
strength_label = Label(window, text="", font=("Helvetica", 14, "bold"), bg="#ffffff")
strength_label.pack(pady=10)

# Generate button
generate_button = Button(window, text="Generate Strong Password", font=("Helvetica", 14), command=lambda: messagebox.showinfo("Generated Password", generate_password()), bg="#1976D2", fg="#ffffff")
generate_button.pack(pady=10)

window.mainloop()
