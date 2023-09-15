


#valid_ip = False

#while False:
 #   ip = input("Please enter a valid IP address: ")
  #  valid_ip = ip_validation(ip)
   # if valid_ip == False:
    #    print("The IP you have entered is invalid.")


print("Please enter a CIDR block number without a slash (optional): /", end="")
cidr = input()
if (validate_cidr(cidr)):
    subnet_mask = calculate_mask(cidr)

if (cidr == ""):
    subnet_mask = calculate_class_mask(ip)


host_or_subnet = input("Calculate per host or per subnet?")
while(True):
if(host_or_subnet == 'subnet'):
    subnets_amount = input("Please enter number of subnets needed: ")
    calculate_hosts(subnets_amount)
elif(host_or_subnet == 'host'):
    hosts_amount = input("Please enter number of hosts per subnet needed: ")
    calculate_subnets(hosts_amount)
else:
    print("Invalid input, please enter again: host/subnet")
    host_or_subnet = input()


