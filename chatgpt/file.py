import os
import requests
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed

class SecureFileDownloader:
    def __init__(self, max_workers=4):
        self.max_workers = max_workers

    def download_file(self, url, dest_folder, expected_checksum=None, retries=3):
        """
        Downloads a file from the given URL and saves it to the destination folder.
        Optionally verifies the file integrity with a provided checksum.
        
        :param url: File URL to download from
        :param dest_folder: Folder where the downloaded file will be saved
        :param expected_checksum: (Optional) SHA256 checksum of the file for integrity verification
        :param retries: Number of retries for failed downloads
        :return: True if the download and verification are successful, otherwise False
        """
        os.makedirs(dest_folder, exist_ok=True)
        local_filename = os.path.join(dest_folder, url.split('/')[-1])
        
        for attempt in range(retries):
            try:
                print(f"Downloading {url}... (Attempt {attempt+1})")
                response = requests.get(url, stream=True, timeout=10)
                response.raise_for_status()  # Raise an error for bad status codes

                with open(local_filename, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)

                if expected_checksum:
                    if not self.verify_checksum(local_filename, expected_checksum):
                        raise ValueError("Checksum mismatch!")
                        
                print(f"Downloaded and verified: {local_filename}")
                return True

            except requests.exceptions.HTTPError as e:
                # Handle specific HTTP errors
                if e.response.status_code == 403:
                    print(f"Access forbidden to {url}. Skipping download.")
                    return False
                elif e.response.status_code == 404:
                    print(f"File not found at {url}. Skipping download.")
                    return False
                else:
                    print(f"Error downloading {url}: {e}")
            
            except requests.RequestException as e:
                print(f"Error downloading {url}: {e}")
            
            if attempt == retries - 1:
                print(f"Failed to download {url} after {retries} attempts.")
                return False

    @staticmethod
    def verify_checksum(file_path, expected_checksum):
        """
        Verifies the checksum of a downloaded file.
        """
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        file_checksum = sha256.hexdigest()
        return file_checksum == expected_checksum

    def download_files(self, url_list, dest_folder, checksums=None):
        """
        Downloads multiple files concurrently using a thread pool.
        """
        checksums = checksums or [None] * len(url_list)
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_url = {
                executor.submit(self.download_file, url, dest_folder, checksums[i]): url
                for i, url in enumerate(url_list)
            }
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    success = future.result()
                    if not success:
                        print(f"Failed to download {url}")
                except Exception as e:
                    print(f"Error occurred while downloading {url}: {e}")

# Example usage
if __name__ == "__main__":
    downloader = SecureFileDownloader(max_workers=4)

    # List of file URLs to download
    file_urls = [
        "https://www.meta.ai/c/dd61720d-2768-4b7d-8fb3-19a7a381f71d.zip",
        "https://chatgpt.com/c/66f804de-21d0-8006-8fc5-e16122d12cf7.zip",
    ]

    # (Optional) Expected checksums for the files
    checksums = [
        "expected_checksum_file1",
        "expected_checksum_file2",
    ]

    destination_folder = "./downloads"
    downloader.download_files(file_urls, destination_folder, checksums)
    