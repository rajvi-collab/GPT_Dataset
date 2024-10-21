import subprocess
import platform
import time

def ping_ip(ip_address, count=4):
    """Ping a specific IP address."""
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, str(count), ip_address]
    
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if output.returncode == 0:
            print(f"Success: {ip_address} is reachable")
        else:
            print(f"Failure: {ip_address} is not reachable")
        print(output.stdout)
    except Exception as e:
        print(f"Error pinging {ip_address}: {e}")

def monitor_ips(ip_list, interval=10):
    """Monitor multiple IPs by pinging them periodically."""
    while True:
        print(f"\n--- Pinging IPs at {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
        for ip in ip_list:
            ping_ip(ip)
        time.sleep(interval)

if __name__ == "__main__":
    # Get user input
    ip_addresses = input("Enter the IP addresses to monitor (comma separated): ").split(',')
    interval = input("Enter the interval (seconds) between pings (default is 10 seconds): ")
    interval = int(interval) if interval else 10

    # Start monitoring
    monitor_ips([ip.strip() for ip in ip_addresses], interval)
