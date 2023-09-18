import math
from network_broadcast import*
def calculate_hosts(number_of_subnets, subnet_mask):
    bin_mask = []
    subnet_list = subnet_mask.split('.')
    for octet in list(subnet_list):
        octet = ipToBin(octet)
        bin_mask.append(octet)
    number_of_zeroes = (''.join(bin_mask)).count('0')
    subnet_power = int(math.log(int(number_of_subnets), 2))

    host_power = number_of_zeroes - subnet_power
    if (host_power <= 0):
        print("Invalid amount of hosts, please choose a larger CIDR block.")

    amount_of_hosts = 2 ** host_power // int(number_of_subnets)
    return amount_of_hosts



