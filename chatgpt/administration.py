import subprocess
import os

class SystemAdminTool:
    def __init__(self):
        self.commands = {
            "1": self.list_files,
            "2": self.current_directory,
            "3": self.change_directory,
            "4": self.system_info,
            "5": self.disk_usage,
            "6": self.network_info,
            "7": self.exit_tool,
        }

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()
            action = self.commands.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again.")

    def display_menu(self):
        print("""
        =======================
        System Admin Tool
        =======================
        1. List Files in Directory
        2. Display Current Directory
        3. Change Directory
        4. Show System Info
        5. Show Disk Usage
        6. Show Network Information
        7. Exit
        """)

    def list_files(self):
        directory = input("Enter directory path (or leave blank for current directory): ").strip() or os.getcwd()
        try:
            files = os.listdir(directory)
            print(f"Files in {directory}:")
            for file in files:
                print(file)
        except FileNotFoundError:
            print("Directory not found.")

    def current_directory(self):
        print(f"Current Directory: {os.getcwd()}")

    def change_directory(self):
        new_dir = input("Enter the path to change to: ").strip()
        try:
            os.chdir(new_dir)
            print(f"Changed to directory: {new_dir}")
        except FileNotFoundError:
            print("Directory not found.")

    def system_info(self):
        try:
            result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            print(f"System Info: \n{result.stdout}")
        except Exception as e:
            print(f"Error fetching system info: {e}")

    def disk_usage(self):
        try:
            result = subprocess.run(['df', '-h'], capture_output=True, text=True)
            print(f"Disk Usage: \n{result.stdout}")
        except Exception as e:
            print(f"Error fetching disk usage: {e}")

    def network_info(self):
        try:
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
            print(f"Network Info: \n{result.stdout}")
        except FileNotFoundError:
            print("Network command not found. Try installing net-tools (Linux).")
        except Exception as e:
            print(f"Error fetching network info: {e}")

    def exit_tool(self):
        print("Exiting tool. Goodbye!")
        exit()

if __name__ == "__main__":
    tool = SystemAdminTool()
    tool.run()
