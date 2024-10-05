import os
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Set the directory where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Configuring the app with the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']

        # If user does not select a file, browser may submit an empty part without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Sanitize the filename
            filename = secure_filename(file.filename)
            
            # Save the file to the specified directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f'File {filename} uploaded successfully!'
        else:
            flash('Invalid file type. Only images are allowed.')
            return redirect(request.url)

    # Render the upload form (for GET request)
    return '''
    <!doctype html>
    <title>Upload an Image</title>
    <h1>Upload a new Image</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
