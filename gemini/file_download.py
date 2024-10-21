import os
import urllib.parse

def download_file(file_path, download_path):
    """Downloads a file from the specified path to the download path.

    Args:
        file_path (str): The path to the file to download.
        download_path (str): The path where the file should be saved.

    Raises:
        ValueError: If the file path is invalid or the file does not exist.
        PermissionError: If there is a permission issue during file creation.
        IOError: If an error occurs during file creation or writing.
    """

    # Validate the file path to prevent path traversal attacks
    if not os.path.isfile(file_path) or not file_path.startswith(os.path.abspath(os.path.join(os.getcwd(), "documents"))):
        raise ValueError("Invalid file path or file does not exist.")

    # Create the download directory if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    # Download the file
    with open(file_path, "rb") as f_in, open(os.path.join(download_path, os.path.basename(file_path)), "wb") as f_out:
        f_out.write(f_in.read())

if __name__ == "__main__":
    file_path = "user_documents/important_document.pdf"
    download_path = "downloads"

    try:
        download_file(file_path, download_path)
        print("File downloaded successfully.")
    except ValueError as e:
        print(f"Error:{e}")
    except (PermissionError, IOError) as e:
        print(f"Error:{e}")
        
        
    
        
    
        
        
    