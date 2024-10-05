import requests
import hashlib
import os

def download_file(url, dest_folder, expected_hash=None):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    local_filename = os.path.join(dest_folder, url.split('/')[-1])
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    if expected_hash:
        if not verify_file_hash(local_filename, expected_hash):
            os.remove(local_filename)
            raise ValueError("File hash does not match expected hash. Download may be corrupted.")
    
    return local_filename

def verify_file_hash(file_path, expected_hash):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    file_hash = sha256.hexdigest()
    return file_hash == expected_hash

def main():
    url = 'https://example.com/file.zip'
    dest_folder = './downloads'
    expected_hash = 'expected_sha256_hash_of_the_file'
    
    try:
        downloaded_file = download_file(url, dest_folder, expected_hash)
        print(f"File downloaded successfully: {downloaded_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
