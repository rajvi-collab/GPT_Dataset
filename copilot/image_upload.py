import os
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration for upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the file upload form
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']

    # If the user does not select a file
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # If the file is valid, save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('upload_form'))

    else:
        flash('Invalid file type. Only image files are allowed.')
        return redirect(request.url)

# Run the Flask app
if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
