import string
from itertools import chain


#def network_broadcast_address(subnet_mask, subnet_amount, ip_address):
subnet_mask = "255.128.0.0"
ip_address = "39.229.177.100"

# These return a list containing the octets, with each octet being stored in a different index altogether in a list
subnet_list = subnet_mask.split('.')
ip_list = ip_address.split('.')

# Initializing lists
bin_subnet_list = []
bin_ip_address_list = []
network_id_chain = []
broadcast_id_chain = []


# Filled in the necessary zeroes while also converting the subnet mask and the ip address to binary
for item in subnet_list:
    item = (bin(int(item))[2:]).zfill(8)
    bin_subnet_list.append(item)
# Filled in the necessary zeroes while also converting the subnet mask and the ip address to binary
for ip in ip_list:
    ip = (bin(int(ip))[2:]).zfill(8)
    bin_ip_address_list.append(ip)

# Converted each list to chains, so that it would be easier
# doing the bitwise calculations as we iterate over each bit at a time
subnet_chain = list(chain.from_iterable(bin_subnet_list))
ip_chain = list(chain.from_iterable(bin_ip_address_list))

# The bitwise calculations between the subnet mask and the ip address.
# we iterate over each of the two in their binary form and do the bitwise
# calculations needed.
for i in range(len(subnet_chain)):
    network_id_chain.append(int((int(subnet_chain[i]) and int(ip_chain[i]))))
    broadcast_id_chain.append(int((int(ip_chain[i]) or (not(int(subnet_chain[i]))))))

# Converts the chain back into a string form and then we iterate over the string
# 8 characters at a time in order to capture the octets. And then we
# concatenate them using the join() function.
# bin_network_id is the binary form of the network id after the calculations
# in a string form with dots separating the octets
binary_string = "".join(str(network_id_chain[i]) for i in range(len(network_id_chain)))
octet = [binary_string[i:i+8] for i in range(0, 32, 8)]
bin_network_id = '.'.join(octet)
# Converts the chain back into a string form and then we iterate over the string
# 8 characters at a time in order to capture the octets. And then we
# concatenate them using the join() function.
# bin_network_id is the binary form of the network id after the calculations
# in a string form with dots separating the octets
binary_string = "".join(str(broadcast_id_chain[j]) for j in range(len(broadcast_id_chain)))
octet = [binary_string[i:i+8] for i in range(0, 32, 8)]
bin_broadcast_id = '.'.join(octet)

# Converts the network id and broadcast id that were calculated above into decimal
# notation.
network_id = ".".join(str(int((bin_network_id[i:i+8]),2)) for i in range(0, 35, 9))
broadcast_id = ".".join(str(int((bin_broadcast_id[i:i+8]),2)) for i in range(0, 35, 9))

print(network_id)
print(broadcast_id)


if(int(network_id.split(".")[-1]) < 255):
    first_host = network_id.split(".")[:3]+([str(int(network_id.split(".")[-1]) + 1)])
    first_host = ".".join(str(first_host[j]) for j in range(len(first_host)))
elif(int(network_id.split(".")[-1]) == 255):
    if(int(network_id.split(".")[-2]) < 255):
        first_host = network_id.split(".")[:2] + ([str(int(network_id.split(".")[-2]) + 1)])
        first_host = ".".join(str(first_host[j]) for j in range(len(first_host)))
    elif(int(network_id.split(".")[-2]) == 255):
        first_host = network_id.split(".")[:1] + ([str(int(network_id.split(".")[-3]) + 1)])
        first_host = ".".join(str(first_host[j]) for j in range(len(first_host)))

# Calculates the last host. Takes the last octet in the broadcast and subtracts one from it
last_host = broadcast_id.split(".")[:3] + [str(int((broadcast_id.split(".")[-1])) - 1)]
last_host = ".".join(str(last_host[j]) for j in range(len(last_host)))

print(first_host)
print(last_host)


# for i in range(len(bin_ip_address_list)):
#     network_id.append((bin_subnet_list[i] and bin_ip_address_list[i]).lstrip('0'))

# print(f'{bin_ip_address_list} bin_ip_address_list')
#
# for i in range(len(bin_ip_address_list)):
#     network_id.append((bin_subnet_list[i] and bin_ip_address_list[i]).lstrip('0'))
#
#
# print(network_id)
#
# for i in range(len(bin_ip_address_list)):
#     print(f'{bin_subnet_list[i]} before not')
#     print(f'{not(bin_subnet_list[i])} after not')
#     broadcast_id.append((bin_ip_address_list[i] or (not (bin_subnet_list[i]))).lstrip('0'))
# print(broadcast_id)








# subnet_chain = list(chain.from_iterable(bin_subnet_list))
# first_zero = subnet_chain.index('0')
#
# # power = count_power(subnet_amount)
# for i in range(first_zero, first_zero + 9):
#     subnet_chain[i] = '1'
#
#
# binary_string = ''.join(subnet_chain)
# octet = [binary_string[i:i+8] for i in range(0, 32, 8)]
# res = '.'.join(octet)
# print(res)
#
# network_class = class_calculate(ip_address)


    #for i in range(power):
     #   string2 = string2 + "1"

    #string2 = string2.ljust(16, "0")
    #power_counter = 0

    #string1 = ""
    #for i in bin_subnet_list[2:]:
    #    string1 = string1 + bin_subnet_list[i]

    #calculated_octets = string1 | string2


   # # for i in range(len(calculated_octets), 8):
   #  #    for octet in bin_subnet_list[2:2 + 2]:
   #          bin_subnet_list[octet] =
   #  for i in ip_list[2:]:
   #      ip_list[2:] = int(bin_subnet_list[2:2 + 2], 2)
   #  binary_ip = '.'.join(binary_octets)




   # print(bin_subnet_list)


    #subnet_counter = subnet_amount
   # while subnet_counter > 0:
      #  if(int(binary_mask[i]) == 0 ):
          #  binary_mask[i] = 1
          #  subnet_counter -= 1



