import math
def calculate_subnets(number_of_hosts, subnet_mask):
    number_of_zeroes = subnet_mask.count("0")
    host_power = int(math.log(number_of_hosts,2)) + 1

    subnet_power = number_of_zeroes - host_power
    if(subnet_power <= 0):
        print("Invalid amount of hosts, please choose a larger CIDR block.")

    amount_of_subnets = 2 ** subnet_power
    return amount_of_subnets



