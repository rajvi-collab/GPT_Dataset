import os
import hashlib
import requests
from requests.exceptions import RequestException

# Custom Exception for download errors
class DownloadError(Exception):
    pass

class SecureFileDownloader:
    def __init__(self, url, dest_file, checksum=None, chunk_size=1024*1024, max_retries=3):
        self.url = url
        self.dest_file = dest_file
        self.chunk_size = chunk_size  # 1MB default chunk size
        self.checksum = checksum      # SHA-256 checksum provided by server
        self.max_retries = max_retries

    def _calculate_checksum(self, file_path):
        """Calculate the SHA-256 checksum of the file."""
        sha256 = hashlib.sha256()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(self.chunk_size), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def _validate_checksum(self):
        """Validate file checksum after download."""
        if not self.checksum:
            return True  # No checksum provided, so skip validation
        calculated_checksum = self._calculate_checksum(self.dest_file)
        return calculated_checksum == self.checksum

    def _get_file_size(self):
        """Query the server for the file size."""
        try:
            response = requests.head(self.url, allow_redirects=True)
            response.raise_for_status()
            return int(response.headers.get('content-length', 0))
        except RequestException as e:
            raise DownloadError(f"Failed to get file size: {e}")

    def _resume_download(self, headers=None):
        """Download the file with support for resuming if it's incomplete."""
        try:
            with requests.get(self.url, stream=True, headers=headers, timeout=10) as response:
                response.raise_for_status()
                with open(self.dest_file, 'ab') as f:
                    for chunk in response.iter_content(chunk_size=self.chunk_size):
                        if chunk:
                            f.write(chunk)
        except RequestException as e:
            raise DownloadError(f"Failed to download file: {e}")

    def download_file(self):
        """Main function to download a file securely."""
        # Get file size from server to check if it's worth resuming
        file_size = self._get_file_size()
        downloaded_size = 0

        # Check if partial file exists and can be resumed
        if os.path.exists(self.dest_file):
            downloaded_size = os.path.getsize(self.dest_file)
            if downloaded_size == file_size:
                print(f"File already downloaded: {self.dest_file}")
                return
            elif downloaded_size < file_size:
                print(f"Resuming download from byte {downloaded_size}...")
        
        headers = {'Range': f'bytes={downloaded_size}-'} if downloaded_size else None

        # Retry logic for network interruptions
        retries = 0
        while retries < self.max_retries:
            try:
                self._resume_download(headers=headers)
                break
            except DownloadError as e:
                retries += 1
                print(f"Retry {retries}/{self.max_retries} - {e}")
        
        # Check if all retries failed
        if retries == self.max_retries:
            raise DownloadError(f"Failed to download file after {self.max_retries} attempts.")

        # Validate checksum after download if provided
        if not self._validate_checksum():
            raise DownloadError("Downloaded file checksum does not match.")
        print(f"File downloaded successfully: {self.dest_file}")

# Example usage:
# downloader = SecureFileDownloader(
#     url="https://example.com/file.zip",
#     dest_file="file.zip",
#     checksum="expected_sha256_checksum"
# )
# downloader.download_file()
