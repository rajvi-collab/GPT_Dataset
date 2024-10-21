import subprocess
import ipaddress

def is_valid_ip(ip: str) -> bool:
    """
    Validates whether the input is a valid IPv4 or IPv6 address.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ping_ip(ip: str):
    """
    Pings the provided IP address securely after validation.
    """
    if not is_valid_ip(ip):
        return f"Invalid IP address: {ip}"

    try:
        # Using subprocess.run to execute the ping command safely
        result = subprocess.run(
            ["ping", "-c", "4", ip],  # For Windows, replace "-c" with "-n"
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            return f"Ping successful for {ip}:\n{result.stdout}"
        else:
            return f"Ping failed for {ip}:\n{result.stderr}"
    
    except Exception as e:
        return f"Error pinging {ip}: {e}"

# Example usage:
ip = "8.8.8.8"  # Replace with the user-provided IP
print(ping_ip(ip))
