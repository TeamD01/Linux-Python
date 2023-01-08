#!/usr/bin/env python
# CHALLENGE: DICTIONARIES

# Create a new script! Have it do the following:
def main():

    # #  Use the char_name and char_stat variables to pull the appropriate value from the dictionary below.
    marvelchars= {
        "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
        "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
        "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
    }

    char_name = ""
    # Save a user's input to the variable char_name from the following question:
    # Which character do you want to know about? (Starlord, Mystique, Hulk)
    
    while(char_name != "q" or char_name != "Q"):
        char_name = input("Which character do you want to know about? (q/Q to quit) ")
        if char_name == "q" or char_name == "Q":
            break
        char_name = char_name.lower().title()  # for Super Bonus 2

        # Save a user's input to the variable char_stat from the following question:
        # What statistic do you want to know about? (real name, powers, archenemy)
        char_stat = input("What statistic do you want to know about? ")

        #Use the char_name and char_stat variables to pull the appropriate value from the dictionary below.
        print(char_name + "'s " + char_stat + " is " + marvelchars.get(char_name).get(char_stat)) 

        # POWER BONUS 1: When returning the hero's real name, have it capitalized appropriately 
        # (e.g. Peter Quill, not peter quill)
        if char_stat == "real name":
            print(char_name + "'s " + char_stat + " is " + marvelchars.get(char_name).get(char_stat).title()) 

        # SUPER BONUS 2: Capitalization matters! Make your script work no matter what capitalization the 
        # user provides!

        # MEGA BONUS 3: Allow the user to try again without exiting the script! Requires previous knowledge 
        # of while loops.
    print("Closing and exiting...")


if __name__ == "__main__":
    main()
