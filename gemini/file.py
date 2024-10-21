import requests
import tqdm
import os

def secure_file_download(url, destination_path, username=None, password=None):
    """Downloads a file securely from a remote server.

    Args:
        url: The URL of the file to download.
        destination_path: The path where the file should be saved.
        username: Optional username for authentication.
        password: Optional password for authentication.
    """

    try:
        response = requests.get(url, auth=(username, password), stream=True)
        response.raise_for_status()

        total_size = int(response.headers.get('content-length', 0))
        with open(destination_path, 'wb') as f:
            with tqdm.tqdm(unit='B', unit_scale=True, total=total_size) as progress:
                for data in response.iter_content(chunk_size=1024):
                    progress.update(len(data))
                    f.write(data)

        print("File downloaded successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

# Example usage:
url = "https://gemini.google.com/app/1eeaff35e3c22774?hl=en-IN.zip"
destination_path = "downloaded_file.zip"
username = "your_username"
password = "your_password"

secure_file_download(url, destination_path, username, password)