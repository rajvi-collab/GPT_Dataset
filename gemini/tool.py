import subprocess
import re

def validate_ip_address(ip_address):
    """Validates an IP address using a regular expression."""
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    return re.match(ip_pattern, ip_address) is not None

def ping_ip(ip_address):
    """Pings an IP address and returns the output."""
    try:
        result = subprocess.run(["ping", "-c", "1", ip_address], capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e}"

def main():
    while True:
        ip_address = input("Enter an IP address to ping (or 'q' to quit): ")
        if ip_address.lower() == 'q':
            break

        if not validate_ip_address(ip_address):
            print("Invalid IP address. Please enter a valid IPv4 address.")
            continue

        ping_result = ping_ip(ip_address)
        print(ping_result)

if __name__ == "__main__":
    main()