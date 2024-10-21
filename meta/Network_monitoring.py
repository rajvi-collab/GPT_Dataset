import os
import platform
import threading
from queue import Queue

class NetworkMonitor:
    def __init__(self):
        self.queue = Queue()
        self.results = {}

    def ping_host(self, ip_address):
        # Ping the host and get the result
        if platform.system().lower() == 'windows':
            ping_cmd = f'ping -n 1 {ip_address}'
        else:
            ping_cmd = f'ping -c 1 {ip_address}'

        response = os.system(ping_cmd)

        # Check the response...
        if response == 0:
            self.results[ip_address] = 'Up'
        else:
            self.results[ip_address] = 'Down'

    def start_monitoring(self, ip_addresses):
        threads = []

        # Create and start threads
        for ip_address in ip_addresses:
            thread = threading.Thread(target=self.ping_host, args=(ip_address,))
            thread.start()
            threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        return self.results


def main():
    monitor = NetworkMonitor()

    # Get IP addresses from user
    num_hosts = int(input("Enter the number of IP addresses to monitor: "))
    ip_addresses = []
    for i in range(num_hosts):
        ip_address = input(f"Enter IP address {i+1}: ")
        ip_addresses.append(ip_address)

    # Start monitoring
    results = monitor.start_monitoring(ip_addresses)

    # Display results
    print("\nMonitoring Results:")
    for ip_address, status in results.items():
        print(f"{ip_address}: {status}")


if __name__ == "__main__":
    main()