import re

def validate_subnet(subnet_mask):
    is_empty = False
    # Check if the input is empty
    if not subnet_mask:
        is_empty = True
        return is_empty

    # Check if the input is a valid CIDR notation (between 1-32)
    subnet_pattern = re.compile(r'^(1\d|[1-9]|[12]\d|32)$')
    return bool(subnet_pattern.match(subnet_mask))


