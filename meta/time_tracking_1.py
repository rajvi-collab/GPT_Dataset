import os
import logging
import datetime
from pathlib import Path
from fpdf import FPDF

# Initialize logger
logging.basicConfig(filename='app.log', level=logging.INFO)

class TimeTrackingApp:
    def __init__(self):
        self.projects = {}

    def add_project(self, project_name):
        """Add a new project."""
        self.projects[project_name] = {'tasks': {}, 'invoices': {}}

    def add_task(self, project_name, task_name, hours_worked):
        """Log time worked on a task."""
        if project_name not in self.projects:
            logging.error(f"Project '{project_name}' does not exist.")
            return

        if task_name not in self.projects[project_name]['tasks']:
            self.projects[project_name]['tasks'][task_name] = 0

        self.projects[project_name]['tasks'][task_name] += hours_worked
        logging.info(f"Added {hours_worked} hours to task '{task_name}' in project '{project_name}'.")

    def generate_invoice(self, project_name, invoice_name):
        """Generate an invoice for a project."""
        if project_name not in self.projects:
            logging.error(f"Project '{project_name}' does not exist.")
            return

        invoice = Invoice(project_name, self.projects[project_name]['tasks'])
        invoice_path = Path(f"invoices/{invoice_name}.pdf")
        invoice.generate_pdf(invoice_path)

        # Validate file path to prevent path traversal
        if not invoice_path.resolve().is_relative_to(Path.cwd()):
            logging.error(f"Invalid invoice path: {invoice_path}")
            return

        logging.info(f"Generated invoice '{invoice_name}' for project '{project_name}'.")

    def export_logs(self, export_path):
        """Export application logs."""
        log_path = Path('app.log')
        export_file_path = Path(export_path)

        # Validate file path to prevent path traversal
        if not export_file_path.resolve().is_relative_to(Path.cwd()):
            logging.error(f"Invalid export path: {export_file_path}")
            return

        with open(log_path, 'r') as log_file, open(export_file_path, 'w') as export_file:
            export_file.write(log_file.read())
        logging.info(f"Exported logs to {export_file_path}.")


class Invoice:
    def __init__(self, project_name, tasks):
        self.project_name = project_name
        self.tasks = tasks

    def generate_pdf(self, invoice_path):
        # Simplified PDF generation using fpdf library
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt=f"Invoice for {self.project_name}", ln=True, align='C')

        for task, hours_worked in self.tasks.items():
            pdf.cell(200, 10, txt=f"{task}: {hours_worked} hours", ln=True, align='L')

        pdf.output(str(invoice_path))


# Example usage:
app = TimeTrackingApp()
app.add_project('Project1')
app.add_task('Project1', 'Task1', 5)
app.add_task('Project1', 'Task2', 3)
app.generate_invoice('Project1', 'invoice1')

