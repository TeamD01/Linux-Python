#!/usr/bin/env python3

#input hostname
hostname = input("What value should we set for hostname? ")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string

# convert to lowercase to remove case sensitive inputs
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
#test for exact match
if hostname == "mtg":
    print("hostname matches expected config")
#exitint message
print("Exiting the script.")
