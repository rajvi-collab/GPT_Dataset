import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

class PDFGenerator:
    def __init__(self, filename, pagesize=letter):
        self.filename = filename
        self.doc = SimpleDocTemplate(filename, pagesize=pagesize)
        self.styles = {}

    def add_style(self, name, font_name, font_size, alignment=TA_LEFT):
        self.styles[name] = ParagraphStyle(
            name=name,
            fontName=font_name,
            fontSize=font_size,
            alignment=alignment,
        )

    def add_text(self, text, style_name):
        self.doc.build([Paragraph(text, self.styles[style_name])])

    def add_table(self, data, style_name):
        table = Table(data)
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('FONTNAME', (0, 0), (-1, -1), style_name),
        ])
        table.setStyle(table_style)
        self.doc.build([table])

    def save(self):
        self.doc.save()

# Example usage
if __name__ == "__main__":
    pdf = PDFGenerator("example.pdf")

    # Add styles
    pdf.add_style("title", "Helvetica-Bold", 24, TA_CENTER)
    pdf.add_style("body", "Helvetica", 12)

    # Add content
    pdf.add_text("PDF Generation Tool", "title")
    pdf.add_text("This is a sample PDF document.", "body")

    # Add table
    data = [
        ["Column 1", "Column 2", "Column 3"],
        ["Row 1, Cell 1", "Row 1, Cell 2", "Row 1, Cell 3"],
        ["Row 2, Cell 1", "Row 2, Cell 2", "Row 2, Cell 3"],
    ]
    pdf.add_table(data, "body")

    # Save PDF
    pdf.save()