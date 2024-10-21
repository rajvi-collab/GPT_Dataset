import os
import hashlib
import secrets
import time
import shutil
from cryptography.fernet import Fernet

UPLOAD_DIR = "uploads"
ENCRYPTED_DIR = "encrypted"
KEY_FILE = "encryption_key.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key


def encrypt_file(filename, key):
    with open(filename, "rb") as f:
        data = f.read()
    encrypted_data = Fernet(key).encrypt(data)
    encrypted_filename = filename + ".enc"
    with open(os.path.join(ENCRYPTED_DIR, encrypted_filename), "wb") as f:
        f.write(encrypted_data)
        
        
def decrypt_file(encrypted_filename, key):
    with open(os.path.join(ENCRYPTED_DIR, encrypted_filename), "rb") as f:
        encrypted_data = f.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    original_filename = encrypted_filename[:-4]
    with open(os.path.join(UPLOAD_DIR, original_filename), "wb") as f:
        f.write(decrypted_data)
        
        
def handle_upload(file):
    # Generate a unique filename based on time and hash
    timestamp = str(int(time.time()))
    file_hash = hashlib.sha256(file.read()).hexdigest()
    filename = f"{timestamp}-{file_hash}-{file.filename}"

    # Save the original file to the upload directory
    file.save(os.path.join(UPLOAD_DIR, filename))

    # Load the encryption key
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

    # Encrypt the file and move it to the encrypted directory
    encrypt_file(os.path.join(UPLOAD_DIR, filename), key)

    # Remove the original file
    os.remove(os.path.join(UPLOAD_DIR, filename))

    return encrypted_filename


def handle_download(encrypted_filename):
    # Load the encryption key
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

    # Decrypt the file and move it to the upload directory
    decrypt_file(encrypted_filename, key)

    # Return the original filename
    return encrypted_filename[:-4]


def main():
    # Create directories if they don't exist
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(ENCRYPTED_DIR, exist_ok=True)

    # Generate encryption key if it doesn't exist
    if not os.path.exists(KEY_FILE):
        generate_key()

    # Handle file uploads and downloads
    # ... (implement your user interface logic here)