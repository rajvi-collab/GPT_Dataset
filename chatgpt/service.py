import subprocess
import shlex

def validate_service_name(service_name):
    """Validate the service name to prevent command injection."""
    # Allowed characters: letters, numbers, and dashes/underscores
    if not all(c.isalnum() or c in ['-', '_'] for c in service_name):
        raise ValueError("Invalid service name: Only letters, numbers, dashes, and underscores are allowed.")

def manage_service(service_name, action):
    """Start or stop a system service."""
    validate_service_name(service_name)
    action_command = f"systemctl {action} {service_name}"

    try:
        # Use shlex to split the command into a list
        command_list = shlex.split(action_command)
        subprocess.run(command_list, check=True)
        print(f"Service '{service_name}' has been {action}ed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to {action} service '{service_name}': {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Service Manager")
    while True:
        service_name = input("Enter the service name (or 'exit' to quit): ").strip()
        if service_name.lower() == 'exit':
            break

        action = input("Enter the action (start/stop): ").strip().lower()
        if action not in ['start', 'stop']:
            print("Invalid action. Please enter 'start' or 'stop'.")
            continue

        manage_service(service_name, action)

if __name__ == "__main__":
    main()
