import re

def validate_subnet(subnet_mask):
    # Check if the input is empty
    if not subnet_mask:
        return True

    # Check if the input is a valid CIDR notation (between 1-32)
    subnet_pattern = re.compile(r'^(1\d|[1-9]|[12]\d|32)$')
    return bool(subnet_pattern.match(subnet_mask))

############# main ###############
while True:
    cidr_input = input("Enter CIDR notation (1-32) or leave empty: ")
    if validate_subnet(cidr_input):
        break  
    else:
        print("Invalid CIDR notation. Must be between 1-32. Please try again.")
