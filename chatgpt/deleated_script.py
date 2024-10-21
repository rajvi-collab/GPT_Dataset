import os
import sys
from pathlib import Path

# Define the list of allowed directories
ALLOWED_DIRECTORIES = [
    Path("/path/to/allowed/directory1"),
    Path("/path/to/allowed/directory2"),
    Path("/path/to/allowed/directory3")
]

def is_safe_path(path: Path) -> bool:
    """Check if the path is within allowed directories."""
    for allowed_dir in ALLOWED_DIRECTORIES:
        try:
            # Resolve paths to avoid relative path tricks and ensure safe paths
            if path.resolve().is_relative_to(allowed_dir.resolve()):
                return True
        except ValueError:
            continue
    return False

def delete_file(file_path: str) -> None:
    """Delete a file after user confirmation."""
    path = Path(file_path).resolve()  # Resolve to handle relative paths
    
    # Check if file exists
    if not path.is_file():
        print(f"Error: {file_path} does not exist or is not a file.")
        return
    
    # Check if the file path is in allowed directories
    if not is_safe_path(path):
        print(f"Error: {file_path} is outside of the allowed directories.")
        return

    # Confirm deletion with the user
    confirmation = input(f"Are you sure you want to delete {file_path}? (yes/no): ")
    if confirmation.lower() == 'yes':
        try:
            path.unlink()  # Delete the file
            print(f"{file_path} has been deleted.")
        except Exception as e:
            print(f"Error: Could not delete the file. Reason: {e}")
    else:
        print("File deletion canceled.")

def main():
    """Main function to handle user input."""
    if len(sys.argv) < 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    delete_file(file_path)

if __name__ == "__main__":
    main()
