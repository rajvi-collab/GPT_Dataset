import argparse
import subprocess
import sys

def parse_args():
    """Parse user input."""
    parser = argparse.ArgumentParser(description='Manage system services.')
    parser.add_argument('action', choices=['start', 'stop', 'restart'], help='Action to perform on the service.')
    parser.add_argument('service_name', help='Name of the service.')
    return parser.parse_args()

def manage_service(action, service_name):
    """Start or stop a system service."""
    try:
        # Use systemd to manage services (for Linux systems)
        command = f"systemctl {action} {service_name}"
        subprocess.check_call(command, shell=True)
        print(f"Service {service_name} {action}ed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to {action} service {service_name}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function."""
    if sys.platform != "linux":
        print("This script is designed for Linux systems.")
        return

    args = parse_args()
    manage_service(args.action, args.service_name)

if __name__ == "__main__":
    main()     