#!/usr/bin/env python3
# ENRICHMENT: Range()
# Handles 1 bottle singular case and no bottles verses

'''
Write a script that will output ALL 99 LINES of the song 99 Bottles of Beer on the Wall! If you're unfamiliar 
with the song, here's what the output would look like:
 99 bottles of beer on the wall!
 99 bottles of beer on the wall! 99 bottles of beer! You take one down, pass it around!
 98 bottles of beer on the wall!
 98 bottles of beer on the wall! 98 bottles of beer! You take one down, pass it around!
 97 bottles of beer on the wall!
 97 bottles of beer on the wall! 97 bottles of beer! You take one down, pass it around!
 [...and so on...]

EXTRA CREDIT 01: include an input() in your script that allows the user to dictate how many bottles 
of beer you're counting down from!

EXTRA CREDIT 02: don't let the user count down from more than 100 bottles of beer.
'''

def main():
    string1 = " bottles of beer on the wall! "
    string2 = " bottles of beer! "
    string3 = " You take one down, pass it around!"
    string4 = " bottle of beer on the wall! "
    string5 = " bottle of beer! "

    verses= int(input("Number of verses to sing (1 - 100) "))
    if verses > 0 and verses <= 100:
        for i in range(verses, 1, -1):
            print(str(i) + string1 + "\n" + str(i) + string1 + str(i) + string2 + string3)
        print("1" + string4 + "\n" + "1" + string4 + " 1" + string5 + " " + string3)
        print("No" + string1)
    else:
        print("Invalid input ~~~ Stop drinking and step away from the keyboard ~~~ bye!!!")

if __name__ == "__main__":
    main()
