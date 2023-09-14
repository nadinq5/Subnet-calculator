

def calculate_mask(ip, CIDR):

    ### convert the subnet mask as a binary string
    binary_mask = "1" * CIDR + "0" * (32 - CIDR)

    ### convert the binary subnet mask to decimal
    subnet_mask = ".".join(
        str(int(binary_mask[i:i + 8], 2))
        for i in range(0, 32, 8)
    )

    return subnet_mask
