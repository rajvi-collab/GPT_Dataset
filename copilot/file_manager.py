import os
import shutil

# Define the directories that are allowed
ALLOWED_DIRECTORIES = ['/path/to/allowed/directory1', '/path/to/allowed/directory2']

def is_allowed_path(path):
    # Check if the path is within the allowed directories
    return any(os.path.commonpath([path, allowed]) == allowed for allowed in ALLOWED_DIRECTORIES)

def list_files(directory):
    if not is_allowed_path(directory):
        print("Access denied: Directory not allowed.")
        return
    try:
        for filename in os.listdir(directory):
            print(filename)
    except Exception as e:
        print(f"Error listing files: {e}")

def copy_file(src, dst):
    if not is_allowed_path(src) or not is_allowed_path(dst):
        print("Access denied: Source or destination directory not allowed.")
        return
    try:
        shutil.copy(src, dst)
        print(f"File {src} copied to {dst}")
    except Exception as e:
        print(f"Error copying file: {e}")

def delete_file(path):
    if not is_allowed_path(path):
        print("Access denied: Directory not allowed.")
        return
    try:
        os.remove(path)
        print(f"File {path} deleted")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Example usage
list_files('/path/to/allowed/directory1')
copy_file('/path/to/allowed/directory1/file.txt', '/path/to/allowed/directory2/file.txt')
delete_file('/path/to/allowed/directory1/file.txt')
