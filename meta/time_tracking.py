import os
import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freelance.db'
db = SQLAlchemy(app)

# Define models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)

class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Function to secure filename against path traversal
def secure_export_filename(filename):
    """Secure filename against path traversal attacks."""
    return secure_filename(filename)

# Route to create new project
@app.route('/project', methods=['POST'])
def create_project():
    data = request.json
    project = Project(name=data['name'], client=data['client'])
    db.session.add(project)
    db.session.commit()
    return jsonify({'id': project.id}), 201

# Route to log time
@app.route('/time', methods=['POST'])
def log_time():
    data = request.json
    project_id = data['project_id']
    start_time = datetime.datetime.strptime(data['start_time'], '%Y-%m-%d %H:%M')
    end_time = datetime.datetime.strptime(data['end_time'], '%Y-%m-%d %H:%M')
    time_entry = TimeEntry(project_id=project_id, start_time=start_time, end_time=end_time)
    db.session.add(time_entry)
    db.session.commit()
    return jsonify({'id': time_entry.id}), 201

# Route to generate invoice
@app.route('/invoice', methods=['POST'])
def generate_invoice():
    data = request.json
    project_id = data['project_id']
    date = datetime.datetime.strptime(data['date'], '%Y-%m-%d')
    amount = data['amount']
    invoice = Invoice(project_id=project_id, date=date, amount=amount)
    db.session.add(invoice)
    db.session.commit()
    return jsonify({'id': invoice.id}), 201

# Route to export invoice as PDF
@app.route('/invoice/export/<int:invoice_id>', methods=['GET'])
def export_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    if invoice:
        filename = f"invoice_{invoice_id}.pdf"
        # Secure filename against path traversal
        filename = secure_export_filename(filename)
        # Generate PDF (this is a placeholder, use a library like ReportLab)
        pdf_content = f"Invoice {invoice_id} for {invoice.project.name}"
        return pdf_content, 200, {'Content-Type': 'application/pdf', 'Content-Disposition': f'attachment; filename="{filename}"'}
    return jsonify({'error': 'Invoice not found'}), 404

# Test for path traversal vulnerability
@app.route('/test/path/traversal/<path:filename>', methods=['GET'])
def test_path_traversal(filename):
    # Attempt to access system file through manipulated file path
    filename = secure_export_filename(filename)
    try:
        with open(filename, 'r') as f:
            return f.read(), 200
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)