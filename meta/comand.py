import subprocess
import argparse

# Define safe commands with their corresponding functions
SAFE_COMMANDS = {
    'backup': lambda: subprocess.run(['tar', '-czf', 'backup.tar.gz', '.']),
    'deploy': lambda: subprocess.run(['git', 'push', 'origin', 'main']),
    'restart': lambda: subprocess.run(['systemctl', 'restart', 'my_service']),
    'update': lambda: subprocess.run(['pip', 'install', '--upgrade', '-r', 'requirements.txt'])
}

def run_command(command):
    """Run a safe command"""
    if command in SAFE_COMMANDS:
        print(f"Running command: {command}")
        SAFE_COMMANDS[command]()
    else:
        print(f"Error: Unknown command '{command}'")

def main():
    parser = argparse.ArgumentParser(description='Deployment Script')
    parser.add_argument('command', type=str, help='Command to run')
    args = parser.parse_args()
    run_command(args.command)

if __name__ == '__main__':
    main()