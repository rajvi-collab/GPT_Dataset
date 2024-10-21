import os
import shutil

def delete_files_in_directory(directory):
    """Deletes all files in the specified directory.

    Args:
        directory (str): The path to the directory to delete files from.
    """

    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory.")
        return

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

def delete_files_in_allowed_directories(allowed_directories):
    """Deletes files in all directories specified in the allowed directories list.

    Args:
        allowed_directories (list): A list of directory paths that are allowed to be deleted from.
    """

    for directory in allowed_directories:
        if os.path.isdir(directory):
            delete_files_in_directory(directory)
        else:
            print(f"Error: '{directory}' is not a directory.")

def get_user_input():
    """Gets user input for the directories to delete files from.

    Returns:
        list: A list of directory paths specified by the user.
    """

    allowed_directories = ["/path/to/directory1", "/path/to/directory2"]   # Replace with your allowed directories
    while True:
        user_input = input("Enter a directory path (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        if user_input in allowed_directories:
            yield user_input
        else:
            print(f"Error: '{user_input}' is not an allowed directory.")

if __name__ == "__main__":
    allowed_directories = ["/path/to/directory1", "/path/to/directory2"]  # Replace with your allowed directories
    delete_files_in_allowed_directories(allowed_directories)
    print("Allowed directories:")
    for directory in allowed_directories:
        print(f"  - {directory}")

    for directory in get_user_input():
        delete_files_in_allowed_directories([directory])