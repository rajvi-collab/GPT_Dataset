import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

class LogViewer:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self.root = tk.Tk()
        self.root.title("Log Viewer")

        # Create frame for log display
        self.log_frame = tk.Frame(self.root)
        self.log_frame.pack(fill="both", expand=True)

        # Create scrolled text box for log display
        self.log_text = scrolledtext.ScrolledText(self.log_frame)
        self.log_text.pack(fill="both", expand=True)

        # Create frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill="x")

        # Create buttons
        self.open_button = tk.Button(self.button_frame, text="Open Log File", command=self.open_log_file)
        self.open_button.pack(side="left")

        self.refresh_button = tk.Button(self.button_frame, text="Refresh", command=self.refresh_logs)
        self.refresh_button.pack(side="left")

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_logs)
        self.clear_button.pack(side="left")

    def open_log_file(self):
        """Open log file dialog and display selected log file"""
        log_file = filedialog.askopenfilename(initialdir=self.log_dir, title="Select Log File")
        if log_file:
            self.display_log_file(log_file)

    def refresh_logs(self):
        """Refresh log display with latest logs"""
        self.clear_logs()
        log_files = self.get_log_files()
        for log_file in log_files:
            self.display_log_file(log_file)

    def clear_logs(self):
        """Clear log display"""
        self.log_text.delete(1.0, tk.END)

    def display_log_file(self, log_file):
        """Display log file contents in log text box"""
        try:
            with open(log_file, 'r') as file:
                log_data = file.read()
                self.log_text.insert(tk.END, log_data)
        except Exception as e:
            self.log_text.insert(tk.END, f"Error reading log file: {str(e)}\n")

    def get_log_files(self):
        """Get list of log files in specified directory"""
        log_files = []
        for file in os.listdir(self.log_dir):
            if file.endswith(".log"):
                log_files.append(os.path.join(self.log_dir, file))
        return log_files

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    log_dir = "/path/to/log/directory"  # Replace with your log directory
    log_viewer = LogViewer(log_dir)
    log_viewer.run()