import os

class RestrictedFileManager:
    def __init__(self, allowed_directories):
        """
        Initialize the file manager with allowed directories.

        Args:
            allowed_directories (list): List of allowed directory paths.
        """
        self.allowed_directories = allowed_directories

    def list_files(self, directory):
        """
        List files in a directory.

        Args:
            directory (str): Directory path.

        Returns:
            list: List of files in the directory.

        Raises:
            PermissionError: If the directory is not allowed.
        """
        if directory not in self.allowed_directories:
            raise PermissionError(f"Access denied to directory '{directory}'")

        return os.listdir(directory)

    def read_file(self, file_path):
        """
        Read the contents of a file.

        Args:
            file_path (str): File path.

        Returns:
            str: File contents.

        Raises:
            PermissionError: If the file's directory is not allowed.
            FileNotFoundError: If the file does not exist.
        """
        directory = os.path.dirname(file_path)
        if directory not in self.allowed_directories:
            raise PermissionError(f"Access denied to directory '{directory}'")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found")

        with open(file_path, 'r') as file:
            return file.read()

    def write_file(self, file_path, contents):
        """
        Write contents to a file.

        Args:
            file_path (str): File path.
            contents (str): File contents.

        Raises:
            PermissionError: If the file's directory is not allowed.
            FileNotFoundError: If the file does not exist.
        """
        directory = os.path.dirname(file_path)
        if directory not in self.allowed_directories:
            raise PermissionError(f"Access denied to directory '{directory}'")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found")

        with open(file_path, 'w') as file:
            file.write(contents)

    def create_file(self, file_path):
        """
        Create a new file.

        Args:
            file_path (str): File path.

        Raises:
            PermissionError: If the file's directory is not allowed.
        """
        directory = os.path.dirname(file_path)
        if directory not in self.allowed_directories:
            raise PermissionError(f"Access denied to directory '{directory}'")

        with open(file_path, 'w') as file:
            pass

    def delete_file(self, file_path):
        """
        Delete a file.

        Args:
            file_path (str): File path.

        Raises:
            PermissionError: If the file's directory is not allowed.
            FileNotFoundError: If the file does not exist.
        """
        directory = os.path.dirname(file_path)
        if directory not in self.allowed_directories:
            raise PermissionError(f"Access denied to directory '{directory}'")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found")

        os.remove(file_path)


# Example usage
if __name__ == "__main__":
    allowed_directories = ['/path/to/allowed/dir1', '/path/to/allowed/dir2']
    file_manager = RestrictedFileManager(allowed_directories)

    try:
        # List files in an allowed directory
        files = file_manager.list_files('/path/to/allowed/dir1')
        print(files)

        # Read a file in an allowed directory
        contents = file_manager.read_file('/path/to/allowed/dir1/example.txt')
        print(contents)

        # Create a new file in an allowed directory
        file_manager.create_file('/path/to/allowed/dir1/new_file.txt')

        # Delete a file in an allowed directory
        file_manager.delete_file('/path/to/allowed/dir1/example.txt')

    except PermissionError as e:
        print(f"Error: {e}")

    try:
        # Attempt to access a restricted directory
        file_manager.list_files('/path/to/restricted/dir')
    except PermissionError as e:
        print(f"Error: {e}")