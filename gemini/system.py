import subprocess
import argparse
import shlex
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description="A system administration tool that executes commands."
    )
    parser.add_argument("command", help="The command to execute")
    parser.add_argument("args", nargs="*", help="Arguments for the command")
    return parser.parse_args()

def execute_command(command, args):
    try:
        command_parts = shlex.split(command)
        command_parts.extend(args)

        process = subprocess.run(command_parts, capture_output=True, text=True)

        if process.returncode == 0:
            print(process.stdout)
        else:
            print(f"Error executing command: {process.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    args = parse_args()
    execute_command(args.command, args.args)

if __name__ == "__main__":
    main()