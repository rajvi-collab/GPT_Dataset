from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

surveys = {}
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/create_survey', methods=['POST'])
def create_survey():
    data = request.json
    survey_id = len(surveys) + 1
    surveys[survey_id] = data
    return jsonify({"message": "Survey created", "survey_id": survey_id})

@app.route('/participate/<int:survey_id>', methods=['POST'])
def participate(survey_id):
    if survey_id not in surveys:
        return jsonify({"message": "Survey not found"}), 404
    response = request.json
    surveys[survey_id].setdefault('responses', []).append(response)
    return jsonify({"message": "Response recorded"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "File uploaded successfully"})
    return jsonify({"message": "File type not allowed"}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
