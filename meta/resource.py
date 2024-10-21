import subprocess
import shlex
import psutil

# Define allowed commands
ALLOWED_COMMANDS = {
    'cpu': 'psutil.cpu_percent',
    'memory': 'psutil.virtual_memory',
    'disk': 'psutil.disk_usage',
    'processes': 'psutil.process_iter'
}

def execute_command(command):
    """Execute a system command and return the output."""
    try:
        output = subprocess.check_output(shlex.split(command))
        return output.decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def get_resource_usage(resource):
    """Get system resource usage."""
    if resource in ALLOWED_COMMANDS:
        if resource == 'cpu':
            return f"CPU usage: {psutil.cpu_percent()}%"
        elif resource == 'memory':
            mem = psutil.virtual_memory()
            return f"Memory usage: {mem.percent}%"
        elif resource == 'disk':
            disk = psutil.disk_usage('/')
            return f"Disk usage: {disk.percent}%"
        elif resource == 'processes':
            processes = [p.info for p in psutil.process_iter(['pid', 'name'])]
            return "\n".join([f"PID: {p['pid']}, Name: {p['name']}" for p in processes])
    else:
        return "Error: Invalid resource command"

def main():
    while True:
        user_input = input("Enter a resource command (cpu, memory, disk, processes, or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        elif user_input in ALLOWED_COMMANDS:
            print(get_resource_usage(user_input))
        else:
            print("Error: Invalid command")

if __name__ == "__main__":
    main()