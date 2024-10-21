import shlex
import subprocess
import sys


def execute_command(command):
    """
    Execute a shell command securely, preventing command injection.
    
    :param command: User-input command to execute
    :return: Tuple containing exit code, stdout, and stderr
    """
    if command.lower() == 'exit':
        sys.exit(0)

    # Split the command into arguments using shlex
    args = shlex.split(command)

    try:
        # Execute the command using subprocess
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Return exit code, stdout, and stderr
        return process.returncode, stdout.decode(), stderr.decode()
    except FileNotFoundError:
        # Handle command not found error
        return 127, "", f"Command '{args[0]}' not found"


def main():
    while True:
        # Get user input
        command = input("Enter a command (or 'exit' to quit): ")

        # Execute the command
        exit_code, stdout, stderr = execute_command(command)

        # Print the results
        print(f"Exit Code: {exit_code}")
        print(f"STDOUT:\n{stdout}")
        print(f"STDERR:\n{stderr}")


if __name__ == "__main__":
    main()