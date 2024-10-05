from fpdf import FPDF

class PDFGenerator:
    def __init__(self, title):
        self.pdf = FPDF()
        self.title = title
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_title(self.title)
        self.pdf.set_font("Arial", size=12)

    def add_title(self, title, font='Arial', size=16, style='B'):
        self.pdf.set_font(font, style, size)
        self.pdf.cell(200, 10, txt=title, ln=True, align='C')
        self.pdf.ln(10)

    def add_paragraph(self, text, font='Arial', size=12):
        self.pdf.set_font(font, size=size)
        self.pdf.multi_cell(0, 10, txt=text)
        self.pdf.ln()

    def add_table(self, data, col_widths=None, font='Arial', size=12):
        self.pdf.set_font(font, size=size)
        if col_widths is None:
            col_widths = [self.pdf.w / len(data[0])] * len(data[0])
        row_height = self.pdf.font_size * 1.5
        for row in data:
            for i, item in enumerate(row):
                self.pdf.cell(col_widths[i], row_height, txt=item, border=1)
            self.pdf.ln(row_height)

    def add_image(self, image_path, x=None, y=None, w=0, h=0):
        self.pdf.image(image_path, x=x, y=y, w=w, h=h)

    def save_pdf(self, filename):
        self.pdf.output(filename)

# Example usage
if __name__ == "__main__":
    pdf = PDFGenerator("Generic PDF Document")
    pdf.add_title("Generic PDF Generation")
    pdf.add_paragraph("This is a sample paragraph to demonstrate generic PDF generation using fpdf2 in Python.")
    pdf.add_table([["Header 1", "Header 2", "Header 3", "Header 4"],
                   ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3", "Row 1 Col 4"],
                   ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3", "Row 2 Col 4"]])
    pdf.add_image("path/to/image.jpg", x=10, y=8, w=100)
    pdf.save_pdf("generic_document.pdf")
