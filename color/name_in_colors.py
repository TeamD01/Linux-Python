#!/usr/bin/env python3
"""Amazon David Monahan
"""
## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""
    
    name = input("What is your name?")

    # print Name in red
    print(crayons.red(name))

    # print Name in magenta
    print(crayons.magenta(name, bold=True))

if __name__ == "__main__":
    main()

