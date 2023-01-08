#!/usr/bin/env python3
# The following code is broken. See if you can rewrite it so that it WORKS

# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def main():
    calc1 = 0.0
    calc2 = 0.0
    operation = ""

    while (calc1 != "q"):
        # Prompt/read value one
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input()
        if calc1 == "q":
            break
        calc1 = float(calc1)

        # Prompt/read value 2
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input()
        if calc2 == "q":
            break
        calc2 = float(calc2)

        # Prompt for operation to be performed
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = input()

        # Select operation and perform it
        if operation == "+":
            print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        elif operation == '-':
            print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
        else:
            print("\n Not a valid entry. Restarting...")

if __name__ == "__main__":
    main()
