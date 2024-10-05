""""""
import re

# Dictionary to store user data for simplicity (in real-world apps, use a database)
users_db = {}

# Email validation function using regular expressions
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Signup function
def signup(email, password):
    if not is_valid_email(email):
        return "Invalid email format."
    
    if email in users_db:
        return "Email is already registered."
    
    # Save the user in the dictionary (passwords should be hashed in real apps)
    users_db[email] = password
    return "Signup successful."

# Signin function
def signin(email, password):
    if not is_valid_email(email):
        return "Invalid email format."
    
    if email not in users_db:
        return "Email not registered."
    
    if users_db[email] != password:
        return "Incorrect password."
    
    return "Signin successful."

# Example usage
def main():
    while True:
        print("\nChoose an option:\n1. Signup\n2. Signin\n3. Exit")
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(signup(email, password))
        
        elif choice == '2':
            email = input("Enter email: ")
            password = input("Enter password: ")
            print(signin(email, password))
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
