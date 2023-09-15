import math
def calculate_hosts(number_of_subnets, subnet_mask):
    number_of_zeroes = subnet_mask.count("0")
    subnet_power = int(math.log(number_of_subnets, 2)) + 1

    host_power = number_of_zeroes - subnet_power
    if (host_power <= 0):
        print("Invalid amount of hosts, please choose a larger CIDR block.")

    amount_of_hosts = 2 ** host_power
    return amount_of_hosts



