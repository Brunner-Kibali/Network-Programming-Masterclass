import sys

# Making sure the IPs are of the required format, and are not reserved addresses; 
# Loopback: 127.0.0.0 - 127.255.255.255
# Multicast: 224.0.0.0 - 239.255.255.255
# Broadcast: 255.255.255.255
# Link-Local: 169.254.0.0 - 169.254.255.255
# Reserved for future use: 240.0.0.0 - 255.255.255.254

# Defining conditions for an IP to be valid
# Checking octets
def ip_addr_valid(list):

    for ip in list:
        # Since each IP is on a different line, when reading the file; each IP will be followed by a \n, e.g ['10.10.10.2\n', '10.10.10.3\n', '10.10.10.4']
        # (we need to strip any character i.e \n to the right of the string using rstrip())
        ip = ip.rstrip("\n")

        # Splitting each IP in the list using . as the delimiter since we need to evaluate each octet below
        # The output is a list of string values e.g ['10', '10', '10', '3']
        octet_list = ip.split(".")

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) \
            and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            
            continue
            
        else:
            print("\n* There was an invalid IP address in the file: {} :(\n".format(ip))
            sys.exit()

    
        


