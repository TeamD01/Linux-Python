#!/usr/bin/env python3

def main():
    string1 = " bottles of beer on the wall! "
    string2 = " bottles of beer! "
    string3 = " You take one down, pass it around!"

    verses= int(input("Number of verses to sing (1 - 100)"))
    if verses > 0 and verses <= 100:
        for i in range(verses, 0, -1):
            print(str(i) + string1 + "\n" + str(i) + string1 + str(i) + string2 + string3)
    else:
        print("Invalid input ~~~ Step away from the keyboard ~~~ bye!!!")
main()
