from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

engine = create_engine('sqlite:///survey_platform.db')
Base = declarative_base()

class Survey(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_active = Column(Boolean, default=True)

# ... rest of the database models

Session = sessionmaker(bind=engine)
session = Session()

# ... Flask forms and views

@app.route('/')
def home():
    # ... home page logic

@app.route('/create_survey', methods=['GET', 'POST'])
def create_survey():
    # ... create survey logic

# ... rest of the routes

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True)