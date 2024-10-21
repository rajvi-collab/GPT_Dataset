import os
import re
import argparse

def parse_log_file(file_path):
    """
    Parse the log file and extract relevant information such as errors, warnings, and other statistics.
    """
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    log_stats = {
        "total_lines": 0,
        "errors": 0,
        "warnings": 0,
        "info": 0
    }

    # Regular expressions for finding log patterns
    error_pattern = re.compile(r"error", re.IGNORECASE)
    warning_pattern = re.compile(r"warning", re.IGNORECASE)
    info_pattern = re.compile(r"info", re.IGNORECASE)

    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                log_stats["total_lines"] += 1
                if error_pattern.search(line):
                    log_stats["errors"] += 1
                elif warning_pattern.search(line):
                    log_stats["warnings"] += 1
                elif info_pattern.search(line):
                    log_stats["info"] += 1
    except Exception as e:
        print(f"Error reading the log file: {e}")
        return

    return log_stats

def display_stats(log_stats, file_path):
    """
    Display the statistics of the log file analysis.
    """
    if log_stats:
        print(f"Log Analysis for {file_path}:")
        print(f"Total Lines: {log_stats['total_lines']}")
        print(f"Errors: {log_stats['errors']}")
        print(f"Warnings: {log_stats['warnings']}")
        print(f"Info: {log_stats['info']}")
    else:
        print(f"No statistics available for {file_path}.")

def main():
    # Argument parser for getting the file path from user input
    parser = argparse.ArgumentParser(description="A log analysis tool.")
    parser.add_argument("file_path", type=str, help="The path to the log file to analyze")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Check if the file exists and then analyze it
    if os.path.isfile(args.file_path):
        log_stats = parse_log_file(args.file_path)
        display_stats(log_stats, args.file_path)
    else:
        print(f"File {args.file_path} does not exist.")

if __name__ == "__main__":
    main()
