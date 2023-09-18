import re

def validate_ip(ip):
    while True:
        ip_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
        if ip_pattern.match(ip):
            return ip
        print("Invalid IP address format. Please enter a valid IP(X.X.X.X), X is a number between 0-255.")
        ip = input("Enter IP Address: ")


