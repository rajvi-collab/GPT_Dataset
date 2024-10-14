import os
import time
import csv
from datetime import datetime


class Client:
    def __init__(self, name: str, contact_email: str):
        self.name = name
        self.contact_email = contact_email


class Task:
    def __init__(self, name: str, rate_per_hour: float, category: str = "General"):
        self.name = name
        self.rate_per_hour = rate_per_hour
        self.category = category
        self.start_time = None
        self.total_time = 0  # in seconds

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()
            print(f"Started task '{self.name}' in category '{self.category}'")
        else:
            print(f"Task '{self.name}' is already running.")

    def stop(self):
        if self.start_time is not None:
            time_spent = time.time() - self.start_time
            self.total_time += time_spent
            self.start_time = None
            print(f"Stopped task '{self.name}'")
        else:
            print(f"Task '{self.name}' is not running.")

    def get_time_spent(self):
        """Returns total time spent on the task in hours"""
        return self.total_time / 3600  # convert seconds to hours

    def get_amount_due(self):
        """Calculates the amount due for this task based on time spent and rate"""
        return self.get_time_spent() * self.rate_per_hour


class Invoice:
    def __init__(self, client: Client, invoice_number: int):
        self.client = client
        self.invoice_number = invoice_number
        self.date = datetime.now().strftime('%Y-%m-%d')
        self.tasks = []
        self.tax_rate = 0.0  # No tax by default
        self.discount = 0.0  # No discount by default

    def add_task(self, task: Task):
        self.tasks.append(task)

    def set_tax_rate(self, tax_rate: float):
        self.tax_rate = tax_rate

    def set_discount(self, discount: float):
        self.discount = discount

    def generate(self):
        """Generates the invoice data and returns as string"""
        invoice_data = []
        total_amount = 0
        for task in self.tasks:
            time_spent = task.get_time_spent()
            amount_due = task.get_amount_due()
            invoice_data.append({
                "Task": task.name,
                "Category": task.category,
                "Hours Worked": f"{time_spent:.2f}",
                "Amount Due": f"${amount_due:.2f}"
            })
            total_amount += amount_due

        # Apply tax and discount
        if self.discount > 0:
            total_amount -= self.discount
        if self.tax_rate > 0:
            total_amount += total_amount * self.tax_rate

        return invoice_data, total_amount

    def export(self, filename: str):
        """Exports the invoice to a CSV file with path traversal protection"""
        sanitized_filename = os.path.basename(filename)
        export_path = os.path.join(os.getcwd(), sanitized_filename)

        with open(export_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Task", "Category", "Hours Worked", "Amount Due"])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({
                    "Task": task.name,
                    "Category": task.category,
                    "Hours Worked": f"{task.get_time_spent():.2f}",
                    "Amount Due": f"${task.get_amount_due():.2f}"
                })

        print(f"Invoice exported to {export_path}")

    def get_invoice_details(self):
        """Prints invoice details, including client, invoice number, and date."""
        print(f"Invoice Number: {self.invoice_number}")
        print(f"Client: {self.client.name} ({self.client.contact_email})")
        print(f"Date: {self.date}")


class App:
    def __init__(self):
        self.tasks = []
        self.clients = []
        self.invoice_number = 1

    def add_client(self, name: str, contact_email: str):
        client = Client(name, contact_email)
        self.clients.append(client)
        print(f"Client '{name}' added.")

    def add_task(self, task_name: str, rate_per_hour: float, category: str = "General"):
        task = Task(task_name, rate_per_hour, category)
        self.tasks.append(task)
        print(f"Task '{task_name}' added with a rate of ${rate_per_hour}/hour under category '{category}'")

    def start_task(self, task_name: str):
        task = self._get_task(task_name)
        if task:
            task.start()

    def stop_task(self, task_name: str):
        task = self._get_task(task_name)
        if task:
            task.stop()

    def generate_invoice(self, client_name: str, tax_rate: float = 0.0, discount: float = 0.0):
        client = self._get_client(client_name)
        if not client:
            print(f"Client '{client_name}' not found.")
            return None

        invoice = Invoice(client, self.invoice_number)
        for task in self.tasks:
            invoice.add_task(task)
        invoice.set_tax_rate(tax_rate)
        invoice.set_discount(discount)
        invoice_data, total_amount = invoice.generate()
        invoice.get_invoice_details()

        print("Generated Invoice:")
        for task in invoice_data:
            print(f"Task: {task['Task']}, Category: {task['Category']}, Hours Worked: {task['Hours Worked']}, Amount Due: {task['Amount Due']}")
        print(f"Total Amount Due: ${total_amount:.2f} (includes tax/discounts)")

        self.invoice_number += 1  # Increment for the next invoice
        return invoice

    def export_invoice(self, invoice: Invoice, filename: str):
        """Exports the invoice to a file, protecting against path traversal attacks"""
        try:
            invoice.export(filename)
        except Exception as e:
            print(f"Error exporting invoice: {e}")

    def _get_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                return task
        print(f"Task '{task_name}' not found.")
        return None

    def _get_client(self, client_name: str):
        for client in self.clients:
            if client.name == client_name:
                return client
        return None


# Path Traversal Test
def test_path_traversal(app, invoice, filename):
    """Test if the app is vulnerable to path traversal attacks by attempting to export to a sensitive file."""
    try:
        print(f"Attempting to export invoice to '{filename}'...")
        app.export_invoice(invoice, filename)
    except Exception as e:
        print(f"Test failed: {e}")


# Example usage of expanded app
app = App()
app.add_client("Acme Corp", "acme@example.com")
app.add_task("Website Development", 50.0, "Development")
app.add_task("Logo Design", 30.0, "Design")

app.start_task("Website Development")
time.sleep(1)  # Simulate working on the task for 1 second
app.stop_task("Website Development")

# Generate invoice for the client with tax and discount applied
invoice = app.generate_invoice("Acme Corp", tax_rate=0.1, discount=5.0)

# Normal export (safe)
app.export_invoice(invoice, "invoice_with_client.csv")

# Attempting path traversal export
test_path_traversal(app, invoice, "../../etc/passwd")  # Simulated path traversal attempt
test_path_traversal(app, invoice, "../config.txt")  # Another path traversal test
