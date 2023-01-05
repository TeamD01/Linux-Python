#!/usr/bin/env python3
import os

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]

os.system('clear')

#Before append
print("\n")
print("Before append (proto): " + str(proto))
print("Before append (protoa): " + str(protoa))
print("\n")

proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list

#After append
print("After append (proto): " + str(proto))
print("After append (protoa): " + str(protoa))
print("\n")

proto2 = [ 22, 80, 443, 53 ] # a list of common ports

#extend proto with proto2
proto.extend(proto2) # pass proto2 as an argument to the extend method
print("Proto after extend method: " + str(proto))

#append protoa with proto2
protoa.append(proto2) # pass proto2 as an argument to the append method
print("Protoa after append method: " + str(protoa))
print("\n")

#insert the string putty into proto and protoa at position 0
proto.insert(0,"putty")
protoa.insert(0,"putty")

print("Proto after insert putty at position 0: " + str(proto))
print("Protoa after insert putty at position 0: " + str(protoa))
print("\n")

print("This is proto2 before sort: " + str(proto2))
proto2.sort()
print("This is proto2 after sort method: " + str(proto2))

proto2.reverse()
print("This is proto2 after reverse sort method: " + str(proto2))
