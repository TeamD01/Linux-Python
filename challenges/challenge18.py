#!/usr/bin/env python3
'''
    CHALLENGE 18: SHEBANG, INPUT, PRINT, CONCATENATE, VARIABLES

Objective: Write a script that contains the following:

    1) An input asking the user's name.

    2) An input asking what day of the week it is.

    3) A print statement that reads:

        Hello, <name>! Happy <day of the week>!
    No cheating... print has to use both inputs, and no "hard coding in" your name and the day 
    in your print function

    BONUS POINTS: no white space weirdness in your output!

    So nothing like this:

        Hello,Chad!   Happy   monday !
'''
def main():
    user_name = input("What is your name: ")
    day_of_week = input("What day is it? i.e. Tuesday: ")
    print("Hello, " + user_name + "! Happy " + day_of_week + "!")

if __name__ == "__main__":
    main()
