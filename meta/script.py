import os

# Define allowed directories
ALLOWED_DIRECTORIES = [
    '/path/to/directory1',
    '/path/to/directory2',
    '/path/to/directory3'
]

def delete_file():
    # Get user input for directory and filename
    directory = input("Enter the directory path: ")
    filename = input("Enter the filename: ")

    # Check if directory is allowed
    if directory not in ALLOWED_DIRECTORIES:
        print("Error: Directory not allowed.")
        return

    # Construct full file path
    filepath = os.path.join(directory, filename)

    # Check if file exists
    if not os.path.isfile(filepath):
        print("Error: File does not exist.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete {filepath}? (y/n): ")
    if confirm.lower() != 'y':
        print("Deletion cancelled.")
        return

    # Delete file
    try:
        os.remove(filepath)
        print(f"File {filepath} deleted successfully.")
    except OSError as e:
        print(f"Error deleting file: {e}")

if __name__ == "__main__":
    delete_file()