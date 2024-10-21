import io
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Table

def generate_pdf(data, template, output_file):
    """Generates a PDF document based on the given data and template.

    Args:
        data: A dictionary containing the data to be included in the PDF.
        template: A dictionary defining the template layout and formatting.
        output_file: The path to the output PDF file.
    """

    # Create a new PDF document
    doc = SimpleDocTemplate(output_file, pagesize=letter)

    # Load the template styles
    styles = getSampleStyleSheet()

    # Create a list to hold the content elements
    content = []

    # Iterate over the template sections
    for section in template['sections']:
        # Create a paragraph for the section title
        title = Paragraph(section['title'], styles['Title'])
        content.append(title)

        # Process the section content based on its type
        if section['type'] == 'text':
            # Create a paragraph for the text content
            text = Paragraph(data[section['data_key']], styles['Normal'])
            content.append(text)
        elif section['type'] == 'image':
            # Create an image element
            image = Image(data[section['data_key']], width=section['width'], height=section['height'])
            content.append(image)
        elif section['type'] == 'table':
            # Create a table element from the data
            table = Table(data[section['data_key']])
            content.append(table)

    # Build the PDF document
    doc.build(content)

# Example usage
data = {
    'title': 'My Report',
    'text': 'This is the main body of the report.',
    'image': 'image.jpg',
    'table': [
        ['Header 1', 'Header 2'],
        ['Data 1', 'Data 2']
    ]
}

template = {
    'sections': [
        {'title': 'Introduction', 'type': 'text', 'data_key': 'text'},
        {'title': 'Image', 'type': 'image', 'data_key': 'image', 'width': 300, 'height': 200},
        {'title': 'Table', 'type': 'table', 'data_key': 'table'}
    ]
}

generate_pdf(data, template, 'output.pdf')