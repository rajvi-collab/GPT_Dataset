import os
import time
from datetime import datetime, timedelta

def sanitize_directory_path(path: str) -> str:
    """
    Sanitize the directory path to prevent command injection.
    Only allow alphanumeric characters, slashes, and periods.
    """
    if not os.path.isdir(path):
        raise ValueError(f"Invalid directory: {path}")
    return os.path.normpath(path)

def delete_old_logs(directory: str, days: int):
    """
    Delete log files older than the specified number of days.
    
    Parameters:
        directory (str): The directory to clean log files from.
        days (int): The age threshold for deleting log files.
    """
    threshold_date = datetime.now() - timedelta(days=days)

    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file and ends with '.log'
        if os.path.isfile(file_path) and filename.endswith('.log'):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))

            # Delete the file if it's older than the threshold date
            if file_mtime < threshold_date:
                print(f"Deleting {file_path} (last modified: {file_mtime})")
                os.remove(file_path)

def main():
    print("Log Cleaning Tool")
    
    # Get the directory and age threshold from the user
    directory = input("Enter the directory containing log files: ")
    days = input("Enter the number of days to keep logs: ")

    try:
        # Sanitize and validate inputs
        sanitized_directory = sanitize_directory_path(directory)
        days = int(days)

        # Proceed with deleting old logs
        delete_old_logs(sanitized_directory, days)
        print("Log cleaning completed.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
