import subprocess

def execute_command(command):
    """Executes a predefined command and returns the output."""
    try:
        # Execute the command
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")

def main():
    # Define a list of safe commands
    safe_commands = {
        'list_files': 'ls -l',  # List files in long format
        'current_directory': 'pwd',  # Print current directory
        'check_disk_space': 'df -h',  # Check disk space
        'current_date': 'date',  # Show current date
    }

    # Display available commands
    print("Available commands:")
    for key in safe_commands.keys():
        print(f"- {key}")

    # Prompt the user for a command
    user_input = input("Enter the command you want to execute: ")

    # Validate user input
    if user_input in safe_commands:
        command_to_execute = safe_commands[user_input]
        execute_command(command_to_execute)
    else:
        print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
