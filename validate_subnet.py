import re

def validate_subnet(subnet_mask):
    # Check if the input is empty (indicating it's optional)
    if not subnet_mask:
        return True

    # Check if the input is a valid CIDR notation (e.g., /1 to /32)
    subnet_pattern = re.compile(r'^\/(1\d|[1-9]|[12]\d|32)$')
    return bool(subnet_pattern.match(subnet_mask))

