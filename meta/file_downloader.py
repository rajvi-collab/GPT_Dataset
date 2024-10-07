import os
import requests
import hashlib
from tqdm import tqdm

class SecureFileDownloader:
    def __init__(self, url, filename, checksum=None):
        """
        Initializes the SecureFileDownloader.

        Args:
            url (str): URL of the file to download.
            filename (str): Local filename to save the downloaded file.
            checksum (str, optional): Expected checksum of the file. Defaults to None.
        """
        self.url = url
        self.filename = filename
        self.checksum = checksum

    def download(self):
        """
        Downloads the file from the remote server.

        Returns:
            bool: True if the download is successful, False otherwise.
        """
        try:
            # Send an HTTP request to the URL and get the response
            response = requests.get(self.url, stream=True)

            # Check if the request was successful
            if response.status_code != 200:
                print(f"Failed to download {self.filename}. Status code: {response.status_code}")
                return False

            # Get the total size of the file
            total_size = int(response.headers.get('content-length', 0))

            # Initialize the progress bar
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

            # Initialize the hash object for checksum calculation
            hash_md5 = hashlib.md5()

            # Open the file in binary write mode
            with open(self.filename, 'wb') as file:
                # Iterate over the chunks of the response
                for chunk in response.iter_content(chunk_size=4096):
                    # Update the progress bar
                    progress_bar.update(len(chunk))

                    # Write the chunk to the file
                    file.write(chunk)

                    # Update the hash object
                    hash_md5.update(chunk)

            # Close the progress bar
            progress_bar.close()

            # Check the checksum if provided
            if self.checksum:
                calculated_checksum = hash_md5.hexdigest()
                if calculated_checksum != self.checksum:
                    print(f"Checksum mismatch for {self.filename}. Expected: {self.checksum}, Calculated: {calculated_checksum}")
                    return False

            print(f"{self.filename} downloaded successfully.")
            return True

        except requests.exceptions.RequestException as e:
            print(f"Error downloading {self.filename}: {e}")
            return False


# Example usage
if __name__ == "__main__":
    url = "https://example.com/file.txt"
    filename = "file.txt"
    checksum = "45a6f2fdd56c2d5a219813c4f7f6f2f2"

    downloader = SecureFileDownloader(url, filename, checksum)
    downloader.download()