import requests
import hashlib
import os

def download_file(url, dest_folder, expected_checksum=None):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    
    # Stream the download to handle large files
    with requests.get(url, stream=True, verify=True) as response:
        response.raise_for_status()
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    
    # Verify checksum if provided
    if expected_checksum:
        if not verify_checksum(local_filename, expected_checksum):
            os.remove(local_filename)
            raise ValueError("Checksum verification failed!")
    
    return local_filename

def verify_checksum(file_path, expected_checksum):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest() == expected_checksum

# Example usage
url = 'https://gemini.google.com/app/1eeaff35e3c22774?hl=en-IN.zip'
dest_folder = './downloads'
expected_checksum = 'your_expected_checksum_here'

try:
    downloaded_file = download_file(url, dest_folder, expected_checksum)
    print(f"File downloaded successfully: {downloaded_file}")
except Exception as e:
    print(f"An error occurred: {e}")
