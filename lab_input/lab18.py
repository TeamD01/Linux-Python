#!/usr/bin/env python3
'''This is Lab 18 Challenge: shebang, input(), print(), concatenate, and variables.
'''

def main():
    "Objective: Write a script that contains the following:

    An input asking the user's name.

    An input asking what day of the week it is.

    A print statement that reads:

        Hello, <name>! Happy <day of the week>! "
    
    user_name_in = input("Enter your name: ")
    day_of_week_in = input("enter the day of the week: ")

    print("Hello, " + user_name_in + "! Happy " + day_of_week_in + "!")

if__name__ == "__main__":
    main()
