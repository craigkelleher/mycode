#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
# this line will add "dns" to the end of our list
proto.append("dns")
# this line will add "dns" to the end of our list
protoa.append("dns")
print(proto)
# Create a list of common ports
proto2 = [ 22, 80, 443, 53 ] 
# pass proto2 as an argument to the extend method
proto.extend(proto2)
print(proto)
# pass proto2 as an aargument to the append method
protoa.append(proto2)
print(protoa)

