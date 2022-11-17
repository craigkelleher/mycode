#!/usr/bin/env python3
# make a list of an IP address, a port, and a status
my_list = [ "192.168.0.5", 5060, "UP" ]
# print the first item in the list, the IP
print("The first item in the list (IP): " + my_list[0] )
# print the second item in the list, the port
print("The second item in the list (port): " + str(my_list[1]))
# print the third item in the list, the status
print("The last item in the list (state): " + my_list[2] )

# display only the IP addresses to the screen.
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

