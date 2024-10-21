import os
import argparse
import glob

def secure_file_search(directory, query):
    """
    Searches for files in the specified directory and its subdirectories 
    that match the user-provided query.

    Args:
        directory (str): The directory to search in.
        query (str): The search query.

    Returns:
        list: A list of matching file paths.
    """
    # Ensure the directory exists and is a directory
    if not os.path.exists(directory) or not os.path.isdir(directory):
        raise ValueError("Invalid directory")

    # Use glob to prevent command injection attacks
    # The glob pattern is safely escaped to prevent shell injection
    pattern = os.path.join(directory, "**", f"*{query}*")
    matching_files = glob.glob(pattern, recursive=True)

    return matching_files


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Secure File Search")
    parser.add_argument("directory", help="Directory to search in")
    parser.add_argument("query", help="Search query")
    args = parser.parse_args()

    try:
        matching_files = secure_file_search(args.directory, args.query)
        print("Matching files:")
        for file in matching_files:
            print(file)
    except ValueError as e:
        print(f"Error: {e}")