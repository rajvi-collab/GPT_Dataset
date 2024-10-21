import os
import argparse
import datetime

def sanitize_input(days):
    """Sanitize user input to prevent command injection"""
    try:
        days = int(days)
        if days < 0:
            raise ValueError
        return days
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        exit(1)

def delete_old_logs(log_dir, days):
    """Delete log files older than specified days"""
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    for filename in os.listdir(log_dir):
        filepath = os.path.join(log_dir, filename)
        if os.path.isfile(filepath):
            file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
            if file_mtime < cutoff_date:
                os.remove(filepath)
                print(f"Deleted: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Log Cleaning Tool")
    parser.add_argument("-d", "--days", required=True, help="Delete logs older than specified days")
    parser.add_argument("-l", "--log-dir", required=True, help="Log directory path")
    args = parser.parse_args()

    days = sanitize_input(args.days)
    log_dir = args.log_dir

    if not os.path.isdir(log_dir):
        print("Invalid log directory.")
        exit(1)

    delete_old_logs(log_dir, days)
    print("Log cleaning completed.")

if __name__ == "__main__":
    main()