

def calculate_mask(ip, CIDR):
    # convert the subnet mask as a binary string
    binary_mask = "1" * CIDR + "0" * (32 - CIDR)
    # this for loop go over the binary_mask and convert every octat to int and covert then in base2 to decimal
    subnet_mask_decimal = ".".join(
        str(int(binary_mask[i:i + 8], 2))
        for i in range(0, 32, 8)
    )

    calced_mask = {
        "ipAdress": ip,
        "subnetMask": subnet_mask_decimal,
        "hosts": 2 ** len("0" * (32 - CIDR))-2,
        "subnets": 2 ** (len("1" * CIDR) % 8)
    }
    return calced_mask

ip = "192.168.1.1"
CIDR = 25
subnet_mask = calculate_mask(ip, CIDR)
print(subnet_mask)

