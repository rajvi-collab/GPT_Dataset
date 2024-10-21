import os
import stat
import hashlib

# Directory where the files will be stored securely
SAVE_DIR = "./secure_uploads/"

# Ensure the directory exists and is only accessible by the owner
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR, exist_ok=True)
    os.chmod(SAVE_DIR, stat.S_IRWXU)  # Read, write, execute only for the owner


def is_safe_filename(filename: str) -> bool:
    """
    Check if the provided filename is safe.
    - No directory traversal (no "..")
    - No absolute paths
    """
    return (
        ".." not in filename
        and not os.path.isabs(filename)
        and os.path.basename(filename) == filename
    )


def generate_secure_filename(filename: str) -> str:
    """
    Generate a secure filename by hashing the original filename.
    This helps avoid collisions and prevents filename guessing.
    """
    name, ext = os.path.splitext(filename)
    hash_name = hashlib.sha256(name.encode('utf-8')).hexdigest()
    return f"{hash_name}{ext}"


def save_secure_file(file_content: bytes, filename: str) -> str:
    """
    Saves the file securely to the specified directory with the secure filename.
    
    Args:
        file_content (bytes): Content of the file to save.
        filename (str): Original filename (to generate secure filename).
    
    Returns:
        str: Full path to the saved file.
    """
    if not is_safe_filename(filename):
        raise ValueError("Unsafe filename provided")

    secure_filename = generate_secure_filename(filename)
    file_path = os.path.join(SAVE_DIR, secure_filename)

    with open(file_path, 'wb') as f:
        f.write(file_content)

    # Set file permission to read/write only for the owner
    os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR)

    return file_path


# Example usage:
if __name__ == "__main__":
    # Example content and filename
    content = b"This is the content of the file."
    original_filename = "user_uploaded_file.txt"

    try:
        saved_file_path = save_secure_file(content, original_filename)
        print(f"File saved securely at: {saved_file_path}")
    except ValueError as e:
        print(f"Error: {e}")
