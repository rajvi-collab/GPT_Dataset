import os
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description="Log Viewer")
    parser.add_argument("directory", help="Directory containing log files")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory.")
        return

    try:
        while True:
            for filename in os.listdir(args.directory):
                if filename.endswith(".log"):
                    with open(os.path.join(args.directory, filename), "r") as f:
                        for line in f:
                            print(line.rstrip())
                    time.sleep(1)  # Adjust the delay as needed
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()