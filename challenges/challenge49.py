#!/usr/bin/env python3
# CHALLENGE- Busted Numbers Game!
import random
'''
Below is a script for a number guessing game! However, it's busted! Please try and get it operational 
(no need to improve it, just make it work).

When working properly, the user should have 5 chances to guess a number that is between 1 and 100. 
The program will tell the user if they guess too high or too low, and if they guess correctly the 
script should end!
'''

#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    num= random.randint(1,100)
    # Pre initialize guess to correct error message below
    guess = -1
    rounds = 0

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines
        # to make sure the number is not a string?
        # Added edge test for [1, 100] range
        if guess.isdigit() and int(guess) > 0 and int(guess) <=100:
            guess= int(guess)
        else:
            print("invalid input...")
            continue

        if guess > num:
            print("Too high! ")
            rounds += 1
            print("You have " + str(5 - rounds) + " guesses left.")

        elif guess < num:
            print("Too low! ")
            rounds += 1
            print("You have " + str(5 - rounds) + " guesses left.")

        else:
            print("Correct! The number was: " + str(num))


# fixing main()
if __name__ == "__main__":
    main()

# First error:
'''
File "/home/student/mycode/challenges/challenge49.py", line 21, in main
    while rounds < 5 and guess != num:
UnboundLocalError: local variable 'guess' referenced before assignment
'''

