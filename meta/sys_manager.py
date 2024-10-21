import subprocess
import os
import argparse
import shlex

def create_folder(folder_name):
    """Create a new folder."""
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def run_command(command):
    """Run a system command."""
    # Use shlex to split the command into arguments, preventing injection
    args = shlex.split(command)
    try:
        # Use subprocess.run with capture_output to prevent output injection
        result = subprocess.run(args, capture_output=True, text=True)
        print(f"Command output: {result.stdout.strip()}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error code {e.returncode}: {e.stderr.strip()}")

def main():
    parser = argparse.ArgumentParser(description="System Resource Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Create folder parser
    folder_parser = subparsers.add_parser("mkdir")
    folder_parser.add_argument("folder_name", help="Name of the folder to create")

    # Run command parser
    command_parser = subparsers.add_parser("run")
    command_parser.add_argument("command", help="System command to run")

    args = parser.parse_args()

    if args.command == "mkdir":
        create_folder(args.folder_name)
    elif args.command == "run":
        run_command(args.command)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()