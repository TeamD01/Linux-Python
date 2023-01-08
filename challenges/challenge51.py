#!/usr/bin/env python3
# Code Repair Challenge!

''' For this challenge, instead of writing code we'll be repairing it. The code block below uses concepts 
we've already learned- lists, dictionaries, methods, functions, built-in functions, and concatenation!
'''
def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name = input('What is your name?\n>')
        num = int(input("Pick a number between 1 and 3: ")) # input returns a string, cast it to an int 

        if name and num in words.keys():
            # If keys and values are in words, print the results
            # The next line is commented out, requres debbugging, and will not run
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name + "! " + "Welcome to Day 2 of Python Training!")

            # in the next line, use title() to capitalize first letter of first/last names
            print("Hi " + name.title() + "! Have a " + words[num] + " day!")
            break

        else:
          print("Come on, follow directions. Try again.")
          continue
        
if __name__ == "__main__":
    main()

