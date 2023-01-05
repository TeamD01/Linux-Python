#!/usr/bin/env python3
"""
1) Create a new script! Have it do the following:

2) Save a user's input to the variable char_name from the following question:
     Which character do you want to know about? (Starlord, Mystique, Hulk)

3) Save a user's input to the variable char_stat from the following question:
    What statistic do you want to know about? (real name, powers, archenemy)

4) Use the char_name and char_stat variables to pull the appropriate value from the dictionary below.

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }
5) Create a print function that combines that information into this output:
 <char_name>'s <char_stat> is: <value> """

def main():
    """runtime function"""

    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")

    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy ")

    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
             }

 
    print(char_name + "'s " + char_stat + " is " + marvelchars.get(char_name).get(char_stat)) 

# call our main function
if __name__ == "__main__":
    main()

