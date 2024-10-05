from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import json
import csv

# Function to create a simple PDF document with basic text, tables, and images
def create_pdf(output_path, data, page_size=A4):
    # Create a document object and specify the output file and page size
    doc = SimpleDocTemplate(output_path, pagesize=page_size)
    
    # Create a list to hold the elements (text, tables, images) to add to the PDF
    elements = []

    # Get predefined styles for consistent formatting
    styles = getSampleStyleSheet()
    
    # Add title or heading
    title = Paragraph("Sample PDF Document", styles['Title'])
    elements.append(title)

    # Add a simple paragraph text
    para = Paragraph("This is a sample PDF generated from various data sources using Python's ReportLab library.", styles['BodyText'])
    elements.append(para)
    
    # If data is in dictionary (e.g., from JSON), convert it into a table
    if isinstance(data, dict):
        table_data = [[key, value] for key, value in data.items()]
        table = Table(table_data)
        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)])
        table.setStyle(style)
        elements.append(table)

    # Example: Adding an image (if provided)
    try:
        img_path = "path/to/image.png"
        img = Image(img_path, 2*inch, 2*inch)
        elements.append(img)
    except Exception as e:
        para = Paragraph(f"Image could not be added: {e}", styles['BodyText'])
        elements.append(para)

    # Build the PDF with the elements added
    doc.build(elements)

# Function to read JSON data
def read_json(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

# Function to read CSV data
def read_csv(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

# Example usage:
json_data = read_json('data.json')
create_pdf('output.pdf', json_data)

csv_data = read_csv('data.csv')
create_pdf('output_csv.pdf', csv_data)
