import datetime

class TimeEntry:
    def __init__(self, project, start_time, end_time, description):
        self.project = project
        self.start_time = start_time
        self.end_time = end_time
        self.description = description

    def duration(self):
        return self.end_time - self.start_time

    def __str__(self):
        return f"{self.project}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')} ({self.duration().total_seconds() / 3600:.2f} hours)"

class Invoice:
    def __init__(self, client, invoice_date):
        self.client = client
        self.invoice_date = invoice_date
        self.time_entries = []

    def add_time_entry(self, time_entry):
        self.time_entries.append(time_entry)

    def total_hours(self):
        return sum(entry.duration().total_seconds() / 3600 for entry in self.time_entries)

    def total_amount(self, hourly_rate):
        return self.total_hours() * hourly_rate

    def generate_invoice(self, hourly_rate):
        invoice_string = f"Invoice for {self.client}\n"
        invoice_string += f"Invoice Date: {self.invoice_date.strftime('%Y-%m-%d')}\n\n"
        invoice_string += "Time Entries:\n"
        for entry in self.time_entries:
            invoice_string += f"  {entry}\n"
        invoice_string += f"\nTotal Hours: {self.total_hours():.2f}\n"
        invoice_string += f"Total Amount: ${self.total_amount(hourly_rate):.2f}\n"
        return invoice_string

def main():
    time_entries = [
        TimeEntry("Project 1", datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 12, 0), "Task 1"),
        TimeEntry("Project 2", datetime.datetime(2023, 10, 2, 10, 0), datetime.datetime(2023, 10, 2, 14, 0), "Task 2"),
        TimeEntry("Project 1", datetime.datetime(2023, 10, 3, 13, 0), datetime.datetime(2023, 10, 3, 17, 0), "Task 3")
    ]

    invoice = Invoice("Client A", datetime.datetime(2023, 10, 10))
    for entry in time_entries:
        invoice.add_time_entry(entry)

    hourly_rate = 50
    invoice_string = invoice.generate_invoice(hourly_rate)
    print(invoice_string)

if __name__ == "__main__":
    main()