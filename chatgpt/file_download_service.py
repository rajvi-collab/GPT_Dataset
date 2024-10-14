from flask import Flask, send_from_directory, abort, request
import os

app = Flask(__name__)

# Directory where files are stored
FILE_DIRECTORY = os.path.abspath("files")

def safe_join(directory, filename):
    """
    Safely join the directory and filename, preventing path traversal.
    This function ensures that the file requested is within the intended directory.
    """
    filepath = os.path.abspath(os.path.join(directory, filename))
    
    # Check if the final path is within the intended directory
    if os.path.commonpath([directory, filepath]) != directory:
        return None
    return filepath

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    """
    Download the file if it exists and is within the allowed directory.
    """
    safe_path = safe_join(FILE_DIRECTORY, filename)
    
    if safe_path and os.path.exists(safe_path):
        return send_from_directory(FILE_DIRECTORY, filename)
    else:
        abort(404)  # File not found or path traversal attempt

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
