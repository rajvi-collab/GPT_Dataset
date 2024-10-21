import os
import argparse

def search_files(directory, filename, extension=None, recursive=False):
    """
    Search for files in a directory.

    Args:
        directory (str): Directory to search in.
        filename (str): Filename to search for.
        extension (str, optional): File extension to filter by. Defaults to None.
        recursive (bool, optional): Search recursively. Defaults to False.

    Returns:
        list: List of matching file paths.
    """
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if filename in file:
                if extension and not file.endswith(extension):
                    continue
                matching_files.append(os.path.join(root, file))
        if not recursive:
            break
    return matching_files

def main():
    parser = argparse.ArgumentParser(description='File Search Tool')
    parser.add_argument('directory', help='Directory to search in')
    parser.add_argument('filename', help='Filename to search for')
    parser.add_argument('-e', '--extension', help='File extension to filter by')
    parser.add_argument('-r', '--recursive', action='store_true', help='Search recursively')
    args = parser.parse_args()
  
    matching_files = search_files(args.directory, args.filename, args.extension, args.recursive)

    if matching_files:
        print('Found matching files:')
        for file in matching_files:
            print(file)
    else:
        print('No matching files found.')

if __name__ == '__main__':
    main()
    
    
    