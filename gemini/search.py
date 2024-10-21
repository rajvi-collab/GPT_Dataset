import os

def search_files(search_params):
    """Searches for files based on given search parameters.

    Args:
        search_params (dict): A dictionary containing search parameters.
            - 'path': The directory to search in.
            - 'filename_pattern': The pattern to match filenames (e.g., '*.txt').
            - 'file_size_min': The minimum file size in bytes.
            - 'file_size_max': The maximum file size in bytes.
            - 'file_creation_time_min': The minimum file creation time as a datetime object.
            - 'file_creation_time_max': The maximum file creation time as a datetime object.
            - 'file_modification_time_min': The minimum file modification time as a datetime object.
            - 'file_modification_time_max': The maximum file modification time as a datetime object.

    Returns:
        list: A list of file paths that match the search criteria.
    """

    results = []

    for root, dirs, files in os.walk(search_params['path']):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_creation_time = os.path.getctime(file_path)
            file_modification_time = os.path.getmtime(file_path)

            if (
                (not search_params['filename_pattern'] or file.endswith(search_params['filename_pattern'])) and
                (not search_params['file_size_min'] or file_size >= search_params['file_size_min']) and
                (not search_params['file_size_max'] or file_size <= search_params['file_size_max']) and
                (not search_params['file_creation_time_min'] or file_creation_time >= search_params['file_creation_time_min']) and
                (not search_params['file_creation_time_max'] or file_creation_time <= search_params['file_creation_time_max']) and
                (not search_params['file_modification_time_min'] or file_modification_time >= search_params['file_modification_time_min']) and
                (not search_params['file_modification_time_max'] or file_modification_time <= search_params['file_modification_time_max'])
            ):
                results.append(file_path)

    return results

def get_search_params():
    """Prompts the user for search parameters and returns them as a dictionary.

    Returns:
        dict: A dictionary containing search parameters.
    """

    search_params = {}
    search_params['path'] = input("Enter the directory to search in: ")
    search_params['filename_pattern'] = input("Enter the filename pattern (e.g., '*.txt'): ")
    search_params['file_size_min'] = int(input("Enter the minimum file size (in bytes): "))
    search_params['file_size_max'] = int(input("Enter the maximum file size (in bytes): "))
    search_params['file_creation_time_min'] = input("Enter the minimum file creation time (YYYY-MM-DD HH:MM:SS): ")
    search_params['file_creation_time_max'] = input("Enter the maximum file creation time (YYYY-MM-DD HH:MM:SS): ")
    search_params['file_modification_time_min'] = input("Enter the minimum file modification time (YYYY-MM-DD HH:MM:SS): ")
    search_params['file_modification_time_max'] = input("Enter the maximum file modification time (YYYY-MM-DD HH:MM:SS): ")

    return search_params

def main():
    search_params = get_search_params()
    results = search_files(search_params)

    if results:
        print("Search results:")
        for result in results:
            print(result)
    else:
        print("No files found.")

if __name__ == "__main__":
    main()