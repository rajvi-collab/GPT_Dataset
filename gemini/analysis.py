import argparse
import re

def analyze_logs(file_paths):
    """Analyzes log files and provides summary statistics."""

    log_data = {}
    error_counts = {}
    warning_counts = {}
    info_counts = {}
    debug_counts = {}

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            for line in f:
                # Extract log level, timestamp, and message
                match = re.match(r'^(?P<level>[A-Z]+)\s+(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s+(?P<message>.*)$', line)
                if match:
                    level = match.group('level')
                    timestamp = match.group('timestamp')
                    message = match.group('message')

                    # Update counts
                    if level not in log_data:
                        log_data[level] = 0
                    log_data[level] += 1

                    if level == 'ERROR':
                        error_counts[timestamp] = error_counts.get(timestamp, 0) + 1
                    elif level == 'WARNING':
                        warning_counts[timestamp] = warning_counts.get(timestamp, 0) + 1
                    elif level == 'INFO':
                        info_counts[timestamp] = info_counts.get(timestamp, 0) + 1
                    elif level == 'DEBUG':
                        debug_counts[timestamp] = debug_counts.get(timestamp, 0) + 1

    # Print summary statistics
    print("Log Analysis Summary:")
    print("---------------------")
    print("Log Level Counts:")
    for level, count in log_data.items():
        print(f"  {level}: {count}")
    print()
    print("Error Counts by Timestamp:")
    for timestamp, count in error_counts.items():
        print(f"  {timestamp}: {count}")
    print()
    print("Warning Counts by Timestamp:")
    for timestamp, count in warning_counts.items():
        print(f"  {timestamp}: {count}")
    print()
    print("Info Counts by Timestamp:")
    for timestamp, count in info_counts.items():
        print(f"  {timestamp}: {count}")
    print()
    print("Debug Counts by Timestamp:")
    for timestamp, count in debug_counts.items():
        print(f"  {timestamp}: {count}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Log Analysis Tool")
    parser.add_argument('file_paths', nargs='+', help='Paths to log files')
    args = parser.parse_args()

    analyze_logs(args.file_paths)