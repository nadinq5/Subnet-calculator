import math
from network_broadcast import*
def calculate_subnets(number_of_hosts, subnet_mask):
    bin_mask = []
    subnet_list = subnet_mask.split('.')
    for octet in list(subnet_list):
        octet = ipToBin(octet)
        bin_mask.append(octet)

    number_of_zeroes = (''.join(bin_mask)).count('0')
    print("THIS IS NUMBER OF ZEROES ",number_of_zeroes)

    host_power = int(math.log(int(number_of_hosts),2)) + 1
    print("HOST POWER ",host_power)

    subnet_power = number_of_zeroes - host_power
    if(subnet_power <= 0):
        print("Invalid amount of hosts, please choose a larger CIDR block.")

    amount_of_subnets = 2 ** subnet_power
    return amount_of_subnets



