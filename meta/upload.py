from flask import Flask, request, jsonify, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads'

class UploadForm(FlaskForm):
    image = FileField('Image', validators=[InputRequired()])
    submit = SubmitField('Upload')

@app.route('/upload', methods=['POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        image = form.image.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': f'Image uploaded successfully: {filename}'}), 201
    else:
        return jsonify({'error': 'Invalid image type'}), 400

if __name__ == '__main__':
    app.run(debug=True)