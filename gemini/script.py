import os

def get_user_input():
    """Gets user input for file operations."""
    while True:
        print("Choose an operation:")
        print("1. Copy a file")
        print("2. Move a file")
        print("3. Rename a file")
        print("4. Delete a file")
        print("5. Create a new file")
        print("6. List files in a directory")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice. Please enter a number between 1 and 7.")
        else:
            return int(choice)

def copy_file():
    """Copies a file to a new location."""
    source_file = input("Enter the source file path: ")
    destination_file = input("Enter the destination file path: ")

    if os.path.exists(source_file):
        try:
            os.copy(source_file, destination_file)
            print("File copied successfully.")
        except Exception as e:
            print("Error copying file:", e)
    else:
        print("Source file does not exist.")

def move_file():
    """Moves a file to a new location."""
    source_file = input("Enter the source file path: ")
    destination_file = input("Enter the destination file path: ")

    if os.path.exists(source_file):
        try:
            os.rename(source_file, destination_file)
            print("File moved successfully.")
        except Exception as e:
            print("Error moving file:", e)
    else:
        print("Source file does not exist.")

def rename_file():
    """Renames a file."""
    old_name = input("Enter the old file name: ")
    new_name = input("Enter the new file name: ")

    if os.path.exists(old_name):
        try:
            os.rename(old_name, new_name)
            print("File renamed successfully.")
        except Exception as e:
            print("Error renaming file:", e)
    else:
        print("Source file does not exist.")

def delete_file():
    """Deletes a file."""
    file_path = input("Enter the file path: ")

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print("File deleted successfully.")
        except Exception as e:
            print("Error deleting file:", e)
    else:
        print("File does not exist.")

def create_file():
    """Creates a new file."""
    file_path = input("Enter the file path: ")

    try:
        with open(file_path, "w") as f:
            pass
        print("File created successfully.")
    except Exception as e:
        print("Error creating file:", e)

def list_files():
    """Lists files in a directory."""
    directory_path = input("Enter the directory path: ")

    if os.path.isdir(directory_path):
        try:
            files = os.listdir(directory_path)
            print("Files in the directory:")
            for file in files:
                print(file)
        except Exception as e:
            print("Error listing files:", e)
    else:
        print("Directory does not exist.")

def main():
    """Main function to handle user input and perform file operations."""
    while True:
        choice = get_user_input()

        if choice == 1:
            copy_file()
        elif choice == 2:
            move_file()
        elif choice == 3:
            rename_file()
        elif choice == 4:
            delete_file()
        elif choice == 5:
            create_file()
        elif choice == 6:
            list_files()
        elif choice == 7:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()