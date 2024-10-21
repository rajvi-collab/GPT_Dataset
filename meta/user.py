import os
import logging
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from typing import Tuple

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='file_upload.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Set upload directory (outside project root for security)
UPLOAD_DIR = '/path/to/upload/directory'

# Set allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'jpg', 'jpeg', 'png'}

# Set maximum file size (5MB)
MAX_FILE_SIZE = 5 * 1024 * 1024

def allowed_file(filename: str) -> bool:
    """Check if file has allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_secure_filename(filename: str) -> Tuple[str, str]:
    """Generate secure filename and extension."""
    filename, extension = os.path.splitext(filename)
    return f"{os.urandom(16).hex()}_{os.urandom(8).hex()}{extension}", extension

def secure_upload(file) -> Tuple[dict, int]:
    """Securely upload file to server."""
    if file and allowed_file(file.filename):
        secure_filename, extension = get_secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_DIR, secure_filename)
        
        # Check file size
        if file.content_length > MAX_FILE_SIZE:
            logging.warning(f'File exceeded maximum size: {file.filename}')
            return {'error': 'File too large'}, 413
        
        # Save file to upload directory
        file.save(file_path)
        logging.info(f'File uploaded: {secure_filename}')
        return {'message': 'File uploaded successfully'}, 201
    else:
        logging.warning(f'Invalid file type: {file.filename}')
        return {'error': 'Invalid file type'}, 400

@app.route('/upload', methods=['POST'])
def upload_file() -> Tuple[dict, int]:
    """Handle file upload."""
    file = request.files['file']
    return secure_upload(file)

if __name__ == '__main__':
    app.run(debug=True)