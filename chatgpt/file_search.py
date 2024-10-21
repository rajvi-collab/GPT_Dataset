import os
import fnmatch

class FileSearchTool:
    def __init__(self, directory: str, extension: str = "*", keyword: str = ""):
        """
        Initialize the search tool with a directory, file extension, and optional keyword.

        :param directory: The directory to search in.
        :param extension: The file extension to filter by (default is all files).
        :param keyword: The keyword to filter files by in the name (default is no keyword).
        """
        self.directory = directory
        self.extension = extension
        self.keyword = keyword

    def search_files(self):
        """
        Search for files in the specified directory based on the given file extension and keyword.

        :return: List of matching file paths.
        """
        matching_files = []

        # Walk through directory and subdirectories
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                # Check if the file matches the extension and keyword
                if fnmatch.fnmatch(file, f"*{self.keyword}*{self.extension}"):
                    matching_files.append(os.path.join(root, file))
        
        return matching_files


# Sample usage:
if __name__ == "__main__":
    # Get user input for directory, file extension, and keyword
    search_dir = input("Enter directory to search: ")
    search_ext = input("Enter file extension to filter by (e.g., .txt, .py) or leave blank for all: ") or "*"
    search_keyword = input("Enter keyword to filter file names or leave blank for all: ") or ""

    # Create the search tool object
    file_search = FileSearchTool(directory=search_dir, extension=search_ext, keyword=search_keyword)

    # Perform search
    results = file_search.search_files()

    # Display results
    if results:
        print("Found files:")
        for file_path in results:
            print(file_path)
    else:
        print("No matching files found.")
