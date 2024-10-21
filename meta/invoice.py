from fpdf import FPDF

class Invoice:
    def __init__(self, project_name, tasks):
        self.project_name = project_name
        self.tasks = tasks

    def generate_pdf(self, invoice_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt=f"Invoice for {self.project_name}", ln=True, align='C')

        for task, hours_worked in self.tasks.items():
            pdf.cell(200, 10, txt=f"{task}: {hours_worked} hours", ln=True, align='L')

        pdf.output(str(invoice_path))
    