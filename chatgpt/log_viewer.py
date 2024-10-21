import os
import glob
from datetime import datetime

class LogViewer:
    def __init__(self, log_dir: str):
        """
        Initialize the log viewer with a specific log directory.
        """
        self.log_dir = log_dir
    
    def list_logs(self):
        """
        List all the log files in the specified directory.
        """
        # Get all log files (assuming logs have a '.log' extension)
        log_files = glob.glob(os.path.join(self.log_dir, "*.log"))
        
        if not log_files:
            print("No log files found.")
            return []
        
        # List all log files
        print("Available log files:")
        for log_file in log_files:
            print(f"- {log_file}")
        
        return log_files
    
    def view_log(self, log_file: str, filter_date: str = None):
        """
        View the content of a specific log file.
        Optionally filter logs by a specific date (in the format YYYY-MM-DD).
        """
        if not os.path.exists(log_file):
            print(f"Log file {log_file} does not exist.")
            return
        
        with open(log_file, "r") as file:
            print(f"\nDisplaying content of: {log_file}\n")
            for line in file:
                if filter_date:
                    # Assuming logs start with a date like "YYYY-MM-DD"
                    if line.startswith(filter_date):
                        print(line.strip())
                else:
                    print(line.strip())
    
    def search_log(self, log_file: str, keyword: str):
        """
        Search for a specific keyword in a log file and display the lines that match.
        """
        if not os.path.exists(log_file):
            print(f"Log file {log_file} does not exist.")
            return
        
        with open(log_file, "r") as file:
            print(f"\nSearching for '{keyword}' in: {log_file}\n")
            found = False
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
                    found = True
            
            if not found:
                print(f"No occurrences of '{keyword}' found.")
    
    def start(self):
        """
        Start the log viewer.
        """
        # Step 1: List logs
        logs = self.list_logs()
        
        if logs:
            # Step 2: Ask user to choose a log file
            log_file = input("\nEnter the log file you want to view: ").strip()
            
            # Check if the file is in the listed logs
            if log_file not in logs:
                print("Invalid log file selected.")
                return
            
            # Step 3: Ask if the user wants to filter by date
            filter_by_date = input("Do you want to filter by date (YYYY-MM-DD)? (y/n): ").strip().lower()
            if filter_by_date == 'y':
                date = input("Enter the date to filter by (YYYY-MM-DD): ").strip()
                self.view_log(log_file, filter_date=date)
            else:
                self.view_log(log_file)
            
            # Step 4: Ask if the user wants to search for a keyword
            search_logs = input("Do you want to search for a keyword in the log? (y/n): ").strip().lower()
            if search_logs == 'y':
                keyword = input("Enter the keyword to search for: ").strip()
                self.search_log(log_file, keyword)

# Example usage
if __name__ == "__main__":
    log_directory = "/path/to/log/directory"  # Replace with the actual path
    viewer = LogViewer(log_directory)
    viewer.start()
