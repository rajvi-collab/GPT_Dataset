import tkinter as tk
from tkinter import messagebox
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk
import random
import time
import datetime

# Create the main window
root = tk.Tk()
root.title("Signup and Login Form")
root.geometry("400x600")

# Function to refresh the CAPTCHA
def refresh_captcha():
    global captcha_text
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    image_captcha = ImageCaptcha()
    captcha_image = image_captcha.generate_image(captcha_text)
    captcha_image.save("captcha.png")
    
    img = Image.open("captcha.png")
    captcha_image_display = ImageTk.PhotoImage(img)
    captcha_label.config(image=captcha_image_display)
    captcha_label.image = captcha_image_display

# Function to display the current time
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=f"Time: {current_time}")
    root.after(1000, update_time)

# Function to validate the form
def validate_form():
    phone = phone_entry.get()
    email = email_entry.get()
    birthdate = birthdate_entry.get()
    entered_captcha = captcha_entry.get()
    
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Invalid phone number!")
        return
    
    if '@' not in email or '.' not in email:
        messagebox.showerror("Error", "Invalid email address!")
        return
    
    try:
        datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Error", "Invalid birthdate format! Use YYYY-MM-DD.")
        return
    
    if entered_captcha != captcha_text:
        messagebox.showerror("Error", "Invalid CAPTCHA!")
        refresh_captcha()
        return
    
    messagebox.showinfo("Success", "Form submitted successfully!")

# Signup Form Title
tk.Label(root, text="Signup Form", font=("Arial", 16)).pack(pady=10)

# Phone Number
tk.Label(root, text="Phone Number").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack()

# Email Address
tk.Label(root, text="Email Address").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack()

# Birthdate
tk.Label(root, text="Birthdate (YYYY-MM-DD)").pack(pady=5)
birthdate_entry = tk.Entry(root)
birthdate_entry.pack()

# CAPTCHA Label and Display
tk.Label(root, text="Enter CAPTCHA:").pack(pady=5)
captcha_entry = tk.Entry(root)
captcha_entry.pack()

captcha_label = tk.Label(root)
captcha_label.pack(pady=5)
refresh_captcha()

# Refresh CAPTCHA Button
refresh_button = tk.Button(root, text="Refresh CAPTCHA", command=refresh_captcha)
refresh_button.pack(pady=5)

# Time Display
time_label = tk.Label(root, text="", font=("Arial", 12))
time_label.pack(pady=10)
update_time()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=validate_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
