#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# python3 -m pip install crayons
import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# CUSTOMIZATION 02
'''
    Create a second function, devicereboot. It should accept a list of IPs as a single argument. The function 
    should iterate through the list IPs, and for each one, print, "Connecting to.. ", then print, "REBOOTING 
    NOW!". Be sure to comment your code.
'''

def devicereboot(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.green("REBOOTING NOW!")}. .. ... ip address is: {ip}') # fstring with RED
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to send command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

# start our main script
def main():
    """called at runtime"""
    with open("devicecmd.json", "r") as devicecmdfile:
        # dict containing IPs mapped to a list of physical interfaces and their state
        devicecmd = json.load(devicecmdfile)

    print(f"\nWelcome to the {crayons.blue('Network')} Device Command Pusher via json") # welcome message with blue text

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd) # Call reboot

# call our main function
main()

