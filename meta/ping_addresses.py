import ping3
import threading
import time

class NetworkMonitor:
    def __init__(self):
        self.ip_addresses = []
        self.ping_interval = 1  # seconds

    def add_ip_address(self, ip_address):
        self.ip_addresses.append(ip_address)

    def remove_ip_address(self, ip_address):
        self.ip_addresses.remove(ip_address)

    def ping_ip_address(self, ip_address):
        while True:
            response = ping3.ping(ip_address)
            if response:
                print(f"{ip_address} is up ({response:.2f} ms)")
            else:
                print(f"{ip_address} is down")
            time.sleep(self.ping_interval)

    def start_monitoring(self):
        threads = []
        for ip_address in self.ip_addresses:
            thread = threading.Thread(target=self.ping_ip_address, args=(ip_address,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


def main():
    monitor = NetworkMonitor()

    while True:
        print("\nNetwork Monitor Menu:")
        print("1. Add IP address")
        print("2. Remove IP address")
        print("3. Start monitoring")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            ip_address = input("Enter IP address: ")
            monitor.add_ip_address(ip_address)
        elif choice == "2":
            ip_address = input("Enter IP address to remove: ")
            if ip_address in monitor.ip_addresses:
                monitor.remove_ip_address(ip_address)
            else:
                print("IP address not found")
        elif choice == "3":
            monitor.start_monitoring()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()