import os
import subprocess

def update_packages(package_names):
    if not package_names:
        print("No package names provided.")
        return

    print(f"Updating the following packages: {', '.join(package_names)}")
    
    try:
        # Step 1: Update the package list
        print("Updating package list...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        
        # Step 2: Upgrade the specified packages
        for package in package_names:
            print(f"Upgrading package: {package}")
            subprocess.run(['sudo', 'apt', 'install', '--only-upgrade', package], check=True)
        
        print("All packages updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while updating packages: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

def main():
    # Get user input for package names (comma-separated)
    user_input = input("Enter package names to update (comma-separated): ")
    package_names = [pkg.strip() for pkg in user_input.split(',') if pkg.strip()]
    
    update_packages(package_names)

if __name__ == "__main__":
    main()
