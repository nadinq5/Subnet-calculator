from class_calculate import*
from calculate_hosts import*
from  calculate_subnets import*
from calculate_mask import*
from network_broadcast import*
from validate_ip import*
from validate_subnet import*



ip_address = input("Enter IP Address: ")
valid_ip = validate_ip(ip_address)

valid_input = False

subnet_class = class_calculator(valid_ip)
subnet_mask = calculate_class_mask(subnet_class)

while not valid_input:
    cidr_input = input("Enter CIDR notation (1-32) or leave empty: ")
    if validate_subnet(cidr_input):
        valid_input = True
    else:
        print("Invalid CIDR notation. Must be between 1-32. Please try again.")
if cidr_input:
    subnet_mask = calculate_cidr_mask(valid_ip, int(cidr_input))

host_or_subnet = input("Calculate per host or per subnet? ")
user_input = True
while(user_input):
    if(host_or_subnet == 'subnet'):
        user_amount = input("Please enter number of subnets needed: ")
        amount = calculate_hosts(user_amount, subnet_mask)
        user_input = False
    elif(host_or_subnet == 'host'):
        user_amount = input("Please enter number of hosts per subnet needed: ")
        amount = calculate_subnets(user_amount, subnet_mask)
        user_input = False
    else:
        print("Invalid input, please enter again: host/subnet")
        host_or_subnet = input()
print("Subnet size: ", amount)
network_broadcast_address(subnet_mask, amount, user_amount, valid_ip)


