import os
import platform
import threading

def ping_ip(ip):
    """
    Pings the given IP address and prints whether it is reachable or not.
    """
    # Determine the command based on the operating system
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Ping command: -c 1 for Linux/macOS, -n 1 for Windows (one packet)
    command = ['ping', param, '1', ip]
    
    # Execute the ping command and check the response
    response = os.system(' '.join(command))
    
    # Check if the IP is reachable
    if response == 0:
        print(f"IP: {ip} is Reachable")
    else:
        print(f"IP: {ip} is Unreachable")


def monitor_ips(ip_list):
    """
    Function to monitor the given list of IPs by pinging each in a separate thread.
    """
    threads = []

    for ip in ip_list:
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Input list of IP addresses from the user
    ip_input = input("Enter the IP addresses (comma separated): ")
    ip_list = [ip.strip() for ip in ip_input.split(",")]
    
    print("\nMonitoring IPs...\n")
    monitor_ips(ip_list)
