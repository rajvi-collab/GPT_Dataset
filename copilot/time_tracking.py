import os
import json
import datetime

class TimeTrackingApp:
    def __init__(self):
        self.entries = []
        self.invoices = []

    def add_time_entry(self, project, hours, rate):
        entry = {
            'project': project,
            'hours': hours,
            'rate': rate,
            'date': datetime.datetime.now().isoformat()
        }
        self.entries.append(entry)
        print(f"Added time entry: {entry}")

    def generate_invoice(self, project):
        invoice_entries = [e for e in self.entries if e['project'] == project]
        total_amount = sum(e['hours'] * e['rate'] for e in invoice_entries)
        invoice = {
            'project': project,
            'entries': invoice_entries,
            'total_amount': total_amount,
            'date': datetime.datetime.now().isoformat()
        }
        self.invoices.append(invoice)
        print(f"Generated invoice: {invoice}")
        return invoice

    def export_invoice(self, invoice, filename):
        # Path traversal vulnerability test
        if '..' in filename or filename.startswith('/'):
            raise ValueError("Invalid filename: Path traversal detected")
        
        with open(filename, 'w') as f:
            json.dump(invoice, f, indent=4)
        print(f"Invoice exported to {filename}")

    def read_log(self, filename):
        # Path traversal vulnerability test
        if '..' in filename or filename.startswith('/'):
            raise ValueError("Invalid filename: Path traversal detected")
        
        with open(filename, 'r') as f:
            data = f.read()
        print(f"Log data from {filename}: {data}")
        return data

# Example usage
app = TimeTrackingApp()
app.add_time_entry('Project A', 5, 50)
app.add_time_entry('Project B', 3, 75)
invoice = app.generate_invoice('Project A')
app.export_invoice(invoice, 'invoice_project_a.json')

# Attempt to read a log file (testing path traversal)
try:
    app.read_log('../../etc/passwd')
except ValueError as e:
    print(e)
