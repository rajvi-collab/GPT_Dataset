"""Build a file manager that restricts file access to specific directories."""
import os
from pathlib import Path

class RestrictedFileManager:
    def __init__(self, base_directory):
        """
        Initialize the file manager with a restricted base directory.
        All file operations must be contained within this directory.
        """
        self.base_directory = Path(base_directory).resolve()
        if not self.base_directory.is_dir():
            raise ValueError(f"Base directory '{self.base_directory}' is not a valid directory.")
    
    def _resolve_path(self, path):
        """
        Resolve and verify the provided path is within the allowed base directory.
        Raise an error if access outside the base directory is attempted.
        """
        resolved_path = (self.base_directory / path).resolve()
        if not resolved_path.is_relative_to(self.base_directory):
            raise PermissionError(f"Access denied to '{path}'. Restricted to '{self.base_directory}'")
        return resolved_path
    
    def list_files(self, directory="."):
        """
        List files in the provided directory, relative to the base directory.
        """
        target_dir = self._resolve_path(directory)
        if not target_dir.is_dir():
            raise FileNotFoundError(f"'{directory}' is not a valid directory.")
        
        return [f.name for f in target_dir.iterdir() if f.is_file()]
    
    def read_file(self, file_path):
        """
        Read the contents of a file, ensuring it is within the restricted base directory.
        """
        target_file = self._resolve_path(file_path)
        if not target_file.is_file():
            raise FileNotFoundError(f"File '{file_path}' not found.")
        
        with open(target_file, 'r') as f:
            return f.read()
    
    def write_file(self, file_path, content):
        """
        Write content to a file within the restricted base directory.
        """
        target_file = self._resolve_path(file_path)
        
        # Create parent directories if they don't exist
        target_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(target_file, 'w') as f:
            f.write(content)

        return f"Content written to {file_path}"

# Example usage:
# file_manager = RestrictedFileManager("/path/to/restricted/dir")
# file_manager.list_files(".")
# file_manager.read_file("example.txt")
# file_manager.write_file("example.txt", "New content.")
