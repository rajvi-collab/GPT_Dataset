import os
import subprocess
import platform
import shutil

def execute_command(command):
    """Execute a command and return the output."""
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def system_info():
    """Return system information."""
    info = {
        'platform': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor()
    }
    return info

def disk_info():
    """Return disk information."""
    info = shutil.disk_usage('/')
    return {
        'total': info.total // (1024.0 ** 3),
        'used': info.used // (1024.0 ** 3),
        'free': info.free // (1024.0 ** 3)
    }

def process_list():
    """Return a list of running processes."""
    command = "ps -aux"
    return execute_command(command)

def main():
    while True:
        print("\nSystem Administration Tool\n")
        print("1. System Information")
        print("2. Disk Information")
        print("3. Process List")
        print("4. Execute Custom Command")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            info = system_info()
            print("\nSystem Information:")
            print(f"Platform: {info['platform']}")
            print(f"Release: {info['release']}")
            print(f"Version: {info['version']}")
            print(f"Architecture: {info['architecture']}")
            print(f"Processor: {info['processor']}")

        elif choice == "2":
            info = disk_info()
            print("\nDisk Information:")
            print(f"Total: {info['total']:.2f} GB")
            print(f"Used: {info['used']:.2f} GB")
            print(f"Free: {info['free']:.2f} GB")

        elif choice == "3":
            print("\nProcess List:")
            print(process_list())

        elif choice == "4":
            command = input("Enter a command: ")
            print("\nOutput:")
            print(execute_command(command))

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()