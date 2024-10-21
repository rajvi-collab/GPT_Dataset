import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_resource_usage(command):
    allowed_commands = {
        'cpu': get_cpu_usage,
        'memory': get_memory_usage,
        'disk': get_disk_usage,
    }

    command = command.lower().strip()
    
    if command in allowed_commands:
        return allowed_commands[command]()
    else:
        return "Invalid command! Allowed commands: 'cpu', 'memory', 'disk'"

def main():
    print("Resource Usage Checker")
    print("Enter 'exit' to quit.")
    
    while True:
        command = input("Enter a command (cpu, memory, disk): ")
        
        if command.lower() == 'exit':
            print("Exiting the program.")
            break
            
        usage = get_resource_usage(command)
        print(f"{command.capitalize()} usage: {usage}%")

if __name__ == "__main__":
    main()
