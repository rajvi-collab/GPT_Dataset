import os
import subprocess
import shlex
import sys

def create_folder(folder_name: str):
    """Create a directory securely"""
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Directory '{folder_name}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")

def run_command(command: str):
    """Run a system command securely after validation"""
    try:
        # Use shlex.split to safely handle user input, preventing injection vulnerabilities
        safe_command = shlex.split(command)
        result = subprocess.run(safe_command, capture_output=True, text=True, check=True)
        print("Command output:\n", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except Exception as e:
        print(f"Error running command: {e}")

def sanitize_input(input_str: str) -> str:
    """Sanitize input to prevent common injection attacks"""
    safe_input = shlex.quote(input_str)  # Quote the input to make it safe for shell
    return safe_input

def main():
    if len(sys.argv) < 2:
        print("Usage: python resource_manager.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == 'create_folder':
        if len(sys.argv) < 3:
            print("Usage: python resource_manager.py create_folder <folder_name>")
            sys.exit(1)
        folder_name = sanitize_input(sys.argv[2])
        create_folder(folder_name)
    
    elif command == 'run_command':
        if len(sys.argv) < 3:
            print("Usage: python resource_manager.py run_command <command>")
            sys.exit(1)
        cmd = sanitize_input(' '.join(sys.argv[2:]))
        run_command(cmd)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
