import pathlib
import re
from datetime import datetime

class LogAnalysisTool:
    def __init__(self, file_path):
        self.file_path = pathlib.Path(file_path)

    def load_log_file(self):
        """Load log file content"""
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return []

    def count_lines(self, log_lines):
        """Count total lines in log file"""
        return len(log_lines)

    def count_errors(self, log_lines):
        """Count error lines in log file"""
        error_pattern = re.compile(r'ERROR|Exception')
        return sum(1 for line in log_lines if error_pattern.search(line))

    def count_warnings(self, log_lines):
        """Count warning lines in log file"""
        warning_pattern = re.compile(r'WARNING')
        return sum(1 for line in log_lines if warning_pattern.search(line))

    def find_longest_request(self, log_lines):
        """Find longest request in log file"""
        request_pattern = re.compile(r'request took (\d+\.\d+) seconds')
        longest_request = 0
        for line in log_lines:
            match = request_pattern.search(line)
            if match:
                request_time = float(match.group(1))
                longest_request = max(longest_request, request_time)
        return longest_request

    def analyze_log(self):
        log_lines = self.load_log_file()
        if log_lines:
            print(f"Log File: {self.file_path}")
            print(f"Total Lines: {self.count_lines(log_lines)}")
            print(f"Error Lines: {self.count_errors(log_lines)}")
            print(f"Warning Lines: {self.count_warnings(log_lines)}")
            longest_request = self.find_longest_request(log_lines)
            if longest_request > 0:
                print(f"Longest Request: {longest_request:.2f} seconds")
            else:
                print("No requests found in log file.")


def main():
    file_path = input("Enter log file path: ")
    tool = LogAnalysisTool(file_path)
    tool.analyze_log()


if __name__ == "__main__":
    main()