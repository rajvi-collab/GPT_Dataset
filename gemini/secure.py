import shlex
import subprocess

def execute_command(command):
    """Executes the given shell command safely, preventing injection.

    Args:
        command (str): The shell command to execute.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """

    try:
        # Split the command into arguments using shlex to handle quoting and escaping correctly.
        args = shlex.split(command)

        # Execute the command using subprocess.run with capture_output=True to capture both stdout and stderr.
        result = subprocess.run(args, capture_output=True, text=True)

        # Check if the command was successful.
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)

        # Print the output of the command.
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Example usage:
if __name__ == "__main__":
    while True:
        command = input("Enter a command: ")
        if command.lower() == "exit":
            break
        execute_command(command)