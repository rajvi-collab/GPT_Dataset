# image_upload_app.py

from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Create Flask app
app = Flask(__name__)

# Designated directory for image uploads
UPLOAD_FOLDER = 'uploads'

# Create uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Configure Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for image upload
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': f'File {filename} uploaded successfully'}), 201
    else:
        return jsonify({'error': 'Unsupported file type'}), 400

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)