import subprocess
import sys

def update_system(package_names):
    """Updates the system with specified packages.

    Args:
        package_names (list): A list of package names to update.
    """

    for package_name in package_names:
        try:
            subprocess.check_call(["sudo", "apt-get", "update", "-y"])
            subprocess.check_call(["sudo", "apt-get", "upgrade", package_name, "-y"])
            print(f"Package '{package_name}' updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error updating package '{package_name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        package_names = sys.argv[1:]
    else:
        package_names = input("Enter package names separated by spaces: ").split()

    update_system(package_names)