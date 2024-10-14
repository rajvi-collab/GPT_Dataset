from flask import Flask, send_from_directory, request, abort
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath("documents")  # Directory where documents are stored

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        # Ensure the requested file is within the BASE_DIR
        requested_path = os.path.abspath(os.path.join(BASE_DIR, filename))
        if not requested_path.startswith(BASE_DIR):
            abort(403)  # Forbidden
        return send_from_directory(BASE_DIR, filename, as_attachment=True)
    except Exception as e:
        abort(404)  # Not Found

if __name__ == '__main__':
    app.run(debug=True)
