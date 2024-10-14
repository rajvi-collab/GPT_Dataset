from flask import Flask, send_file, safe_join
import os

app = Flask(__name__)

# Define the directory where files are stored
FILE_DIRECTORY = 'files'

@app.route('/download/<path:filename>')
def download_file(filename):
    """
    Download a file from the files directory.

    Args:
        filename (str): The name of the file to download.

    Returns:
        A Flask response object containing the file.
    """
    file_path = safe_join(FILE_DIRECTORY, filename)
    if not os.path.isfile(file_path):
        return f'File {filename} not found', 404

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)