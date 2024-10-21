import os
import subprocess
import shlex

def create_folder(path):
    try:
        os.makedirs(path)
        print(f"Folder created successfully at {path}")
    except OSError as e:
        print(f"Error creating folder: {e}")

def run_command(command):
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True)
        print(f"Command output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

def main():
    while True:
        print("Choose an action:")
        print("1. Create a folder")
        print("2. Run a command")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter the folder path: ")
            create_folder(path)
        elif choice == "2":
            command = input("Enter the command: ")
            run_command(command)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()