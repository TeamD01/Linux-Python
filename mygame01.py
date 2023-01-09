#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win!
    Avoid the monsters! Commands include go direction and get item.
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'west'  : 'Bedroom',
                  'item'  : 'key'
                },
            'Bedroom' : {
                'east' : 'Hall',
                'north' : 'Secret Room',
                'item' : 'null pointer'
                },
            'Secret Room' :{
                'south' : 'Bedroom',
                'north' : 'Mall',
                'item' : 'credit card zach feeser'
                },
            'Mall' :{
                'south' : 'Secret Room'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room'
            }
         }
# start the player in the Hall
currentRoom = 'Hall'
count = 0
showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #teleport
    if move[0] == 'teleport':
        currentRoom = move[1].title()

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            count+=1
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')
        print("Number of moves is: " + str(count))
    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## Alternate ending
    if currentRoom == 'Mall' and 'credit card zach feeser' in inventory:
        print("You excaped to the Mall with Zach's credit card... SHOPPING!!!")
        break
