import subprocess
import pkg_resources

def update_packages(package_names):
    """
    Updates the specified packages using pip.

    Args:
    package_names (list): List of package names to update.
    """
    try:
        for package_name in package_names:
            subprocess.check_call(['pip', 'install', '--upgrade', package_name])
            print(f"{package_name} updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update {package_name}: {e}")

def get_user_input():
    """
    Gets package names from user input.

    Returns:
    list: List of package names.
    """
    package_names = input("Enter package names separated by space: ")
    return package_names.split()

def main():
    package_names = get_user_input()
    update_packages(package_names)

if __name__ == "__main__":
    main()