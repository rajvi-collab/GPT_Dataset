import subprocess
import ipaddress
import argparse

def validate_ip(address):
    """Validate IP address"""
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

def ping_ip(address):
    """Ping IP address"""
    if validate_ip(address):
        try:
            # Use subprocess.run to execute the ping command
            # The input is sanitized by validate_ip, so it's safe to use
            result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{address} is reachable")
            else:
                print(f"{address} is unreachable")
        except Exception as e:
            print(f"Error pinging {address}: {e}")
    else:
        print(f"Invalid IP address: {address}")

def main():
    parser = argparse.ArgumentParser(description="Secure Ping Tool")
    parser.add_argument("ip", help="IP address to ping")
    args = parser.parse_args()
    ping_ip(args.ip)

if __name__ == "__main__":
    main()