import os
import fnmatch

def safe_search_files(directory, search_pattern):
    # Ensure that the directory is absolute and valid
    if not os.path.isdir(directory):
        raise ValueError("The provided directory does not exist or is not a directory.")
    
    # Escape the search pattern to avoid injection
    search_pattern = fnmatch.translate(search_pattern)
    
    found_files = []
    
    # Walk through the directory
    for dirpath, _, files in os.walk(directory):
        for filename in files:
            if fnmatch.fnmatch(filename, search_pattern):
                found_files.append(os.path.join(dirpath, filename))

    return found_files

def main():
    print("Welcome to the Safe File Search Utility.")
    directory = input("Enter the directory to search in: ").strip()
    search_pattern = input("Enter the file name pattern to search for (e.g., '*.txt'): ").strip()
    
    try:
        results = safe_search_files(directory, search_pattern)
        if results:
            print(f"Found {len(results)} file(s):")
            for file in results:
                print(file)
        else:
            print("No files found matching the pattern.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
