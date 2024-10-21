import os

def create_file(filename):
    """Create a new file."""
    try:
        open(filename, 'w').close()
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")


def read_file(filename):
    """Read and display the contents of a file."""
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def write_to_file(filename):
    """Write user input to a file."""
    try:
        user_input = input("Enter text to write to file: ")
        with open(filename, 'a') as file:
            file.write(user_input + "\n")
        print(f"Text appended to '{filename}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")


def delete_file(filename):
    """Delete a file."""
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error deleting file: {e}")


def list_files():
    """List all files in the current directory."""
    try:
        print("Files in the current directory:")
        for file in os.listdir():
            if os.path.isfile(file):
                print(file)
    except Exception as e:
        print(f"Error listing files: {e}")


def main():
    while True:
        print("\nFile Operations Menu:")
        print("1. Create File")
        print("2. Read File")
        print("3. Write to File")
        print("4. Delete File")
        print("5. List Files")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            filename = input("Enter filename: ")
            create_file(filename)
        elif choice == "2":
            filename = input("Enter filename: ")
            read_file(filename)
        elif choice == "3":
            filename = input("Enter filename: ")
            write_to_file(filename)
        elif choice == "4":
            filename = input("Enter filename: ")
            delete_file(filename)
        elif choice == "5":
            list_files()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()