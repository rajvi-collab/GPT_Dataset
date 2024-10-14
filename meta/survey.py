from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///survey.db"
app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

db = SQLAlchemy(app)


class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    options = db.relationship("Option", backref="survey", lazy=True)


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"), nullable=False)


class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey("survey.id"), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey("option.id"), nullable=False)


@app.route("/create_survey", methods=["POST"])
def create_survey():
    data = request.get_json()
    survey = Survey(title=data["title"])
    db.session.add(survey)
    db.session.commit()
    for option in data["options"]:
        db_option = Option(text=option, survey_id=survey.id)
        db.session.add(db_option)
    db.session.commit()
    return jsonify({"message": "Survey created successfully"}), 201


@app.route("/participate/<int:survey_id>", methods=["POST"])
def participate(survey_id):
    data = request.get_json()
    vote = Vote(survey_id=survey_id, option_id=data["option_id"])
    db.session.add(vote)
    db.session.commit()
    return jsonify({"message": "Vote recorded successfully"}), 200


@app.route("/export_survey_data/<int:survey_id>", methods=["GET"])
def export_survey_data(survey_id):
    survey = Survey.query.get(survey_id)
    data = []
    for option in survey.options:
        data.append({"text": option.text, "votes": len(option.votes)})
    return jsonify(data)


@app.route("/upload_file", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return jsonify({"message": "File uploaded successfully"}), 201


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)