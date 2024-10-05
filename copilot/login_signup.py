import tkinter as tk
from tkinter import messagebox
import re
from captcha.image import ImageCaptcha
import random
import time

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def generate_captcha():
    image = ImageCaptcha()
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
    image.write(captcha_text, 'captcha.png')
    return captcha_text

def signup():
    email = email_entry.get()
    phone = phone_entry.get()
    birthdate = birthdate_entry.get()
    captcha_input = captcha_entry.get()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email address")
        return

    if captcha_input != captcha_text:
        messagebox.showerror("Error", "Invalid CAPTCHA")
        return

    messagebox.showinfo("Success", f"Signup successful!\nTime: {current_time}")

def login():
    # Implement login functionality here
    pass

app = tk.Tk()
app.title("Login and Signup Form")

tk.Label(app, text="Email:").grid(row=0, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=0, column=1)

tk.Label(app, text="Phone Number:").grid(row=1, column=0)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

tk.Label(app, text="Birthdate (YYYY-MM-DD):").grid(row=2, column=0)
birthdate_entry = tk.Entry(app)
birthdate_entry.grid(row=2, column=1)

captcha_text = generate_captcha()
tk.Label(app, text="CAPTCHA:").grid(row=3, column=0)
captcha_entry = tk.Entry(app)
captcha_entry.grid(row=3, column=1)
tk.Label(app, text=f"Enter CAPTCHA: {captcha_text}").grid(row=4, column=0, columnspan=2)

tk.Button(app, text="Signup", command=signup).grid(row=5, column=0, columnspan=2)
tk.Button(app, text="Login", command=login).grid(row=6, column=0, columnspan=2)

app.mainloop()
