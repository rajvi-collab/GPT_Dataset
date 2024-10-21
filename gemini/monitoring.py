import subprocess
import argparse
import time

def ping(ip_address):
    """Pings an IP address and returns the result."""
    try:
        result = subprocess.run(["ping", "-c", "4", ip_address], capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def main():
    parser = argparse.ArgumentParser(description="Ping multiple IP addresses.")
    parser.add_argument("ip_addresses", nargs="+", help="IP addresses to ping")
    parser.add_argument("-i", "--interval", type=int, default=1, help="Ping interval in seconds")
    args = parser.parse_args()

    while True:
        for ip_address in args.ip_addresses:
            result = ping(ip_address)
            print(f"Pinging {ip_address}:")
            print(result)

        time.sleep(args.interval)

if __name__ == "__main__":
    main()