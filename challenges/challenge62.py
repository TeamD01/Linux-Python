#!/usr/bin/env python3
# "Looping with for" Challenge!

# Part 1
# • Write a for loop that returns all the animals from the NE Farm!

# Part 2
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised 
#on that farm.

# Part 3
# • Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that 
# particular farm.

# SUPER BONUS  We need to change index of part 1 to point to Northeast Farm [1] instead of [0]
'''Test the flexibility of your code... does it still work if you swap the value of farms for this?

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]
'''

def main():

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    yuck= ["carrots", "celery", "bananas", "apples", "oranges"]
    NE_animals= farms[0]["agriculture"]
    print("Part 1: The animals from the NE Farm are: ")
    for animal in NE_animals:
        print("\t" + animal)

    print("\nPart 2: Choose a farm and return the plants/animals")
    print("The current farms are: ")
    for farm in farms:
        print("\t", farm["name"])
    choice= input("\nSelect a farm: ")
    print("The plants and animals from the " + choice + " farm are: ")
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                print("\t" + ag_item)

    print("\nPart3: Choose farm and return only animals ")
    print("The current farms are: ")
    for farm in farms:
        print("\t", farm["name"])
    choice= input("\nSelect a farm: ")
    print("The animals from the " + choice + " farm are: ")
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in yuck:
                    print("\t" + ag_item)

    print("\nSUPER BONUS: Does it still work for swapped values of farms? ")
    farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


    NE_animals= farms[1]["agriculture"]
    print("Part 1: The animals from the Northeast Farm are: ")
    for animal in NE_animals:
        print("\t" + animal)

    print("\nPart 2: Choose a farm and return the plants/animals")
    print("The current farms are: ")
    for farm in farms:
        print("\t", farm["name"])
    choice= input("\nSelect a farm: ")
    print("The plants and animals from the " + choice + " farm are: ")
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                print("\t" + ag_item)

    print("\nPart3: Choose farm and return only animals ")
    print("The current farms are: ")
    for farm in farms:
        print("\t", farm["name"])
    choice= input("\nSelect a farm: ")
    print("The animals from the " + choice + " farm are: ")
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in yuck:
                    print("\t" + ag_item)



if __name__ == "__main__":
    main()
