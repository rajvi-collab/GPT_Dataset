import os
import shutil
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the desired upload directory
upload_dir = "uploads"

# Create the upload directory if it doesn't exist
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)   


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # Check   
 if the file is empty
    if file.filename == '':
        return 'No selected   
 file'

    # Ensure the file has an allowed extension (e.g., .jpg, .png)
    allowed_extensions = set(['jpg', 'png'])
    file_extension = file.filename.rsplit('.', 1)[1].lower()
    if file_extension not in allowed_extensions:
        return 'Invalid file extension'

    # Generate a secure filename to prevent potential security issues
    filename = secure_filename(file.filename)

    # Save the file to the upload directory
    file_path = os.path.join(upload_dir, filename)
    file.save(file_path)

    return 'File uploaded successfully!'

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(upload_dir, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File not found'

if __name__ == '__main__':
    app.run(debug=True)