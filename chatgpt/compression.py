import os
import zipfile
from pathlib import Path

def safe_path_check(base_path, target_path):
    """Ensure the target path is within the base directory to avoid directory traversal attacks."""
    base_path = os.path.abspath(base_path)
    target_path = os.path.abspath(target_path)
    return os.path.commonpath([base_path]) == os.path.commonpath([base_path, target_path])

def zip_directory(source_dir, output_zip):
    """
    Compress the specified directory into a ZIP file.
    
    Parameters:
    - source_dir: The directory to compress
    - output_zip: The path to the output zip file
    """
    # Ensure source_dir exists and is a directory
    source_dir = Path(source_dir)
    if not source_dir.is_dir():
        raise ValueError(f"Source directory '{source_dir}' does not exist or is not a directory.")
    
    # Creating ZIP file
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(source_dir):
            for file in files:
                file_path = Path(root) / file

                # Sanity check for security: Ensure no directory traversal outside of source_dir
                if not safe_path_check(source_dir, file_path):
                    raise ValueError(f"Illegal path detected: {file_path}")
                
                # Add file to the ZIP file, preserving relative paths
                zipf.write(file_path, file_path.relative_to(source_dir))

def main():
    source_dir = input("Enter the directory to compress: ").strip()
    output_zip = input("Enter the path for the output zip file (e.g., archive.zip): ").strip()

    try:
        zip_directory(source_dir, output_zip)
        print(f"Directory '{source_dir}' has been successfully compressed into '{output_zip}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
