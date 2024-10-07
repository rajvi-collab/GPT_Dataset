import subprocess

def ping_ip(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, universal_newlines=True)
        if "1 packets transmitted, 1 received" in output:
            return f"{ip} is reachable"
        else:
            return f"{ip} is not reachable"
    except subprocess.CalledProcessError:
        return f"{ip} is not reachable"

def main():
    ip_addresses = input("Enter IP addresses separated by spaces: ").split()
    for ip in ip_addresses:
        status = ping_ip(ip)
        print(status)

if __name__ == "__main__":
    main()
