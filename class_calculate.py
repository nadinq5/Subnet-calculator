def class_calculator(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'The IP address {ip} belongs to Class A'
    elif 128 <= first_octet <= 191:
        return 'The IP address {ip} belongs to Class B'
    elif 192 <= first_octet <= 223:
        return 'The IP address {ip} belongs to Class C'
    elif 224 <= first_octet <= 239:
        return 'The IP address {ip} belongs to Class D'
    elif 240 <= first_octet <= 255:
        return 'The IP address {ip} belongs to Class E'
    elif first_octet == 127:
        return 'The IP address {ip} is Loopback'
    else:
        return None
