#!/usr/bin/python

# Spooky Loopin' Exercise

# Run the following command to download the book Dracula by Bram Stoker. Yes, the whole thing!

# wget https://www.gutenberg.org/files/345/345-0.txt -qO dracula.txt

def main():
    
    # Part 1
    # Read in the content of the Dracula novel as a file object.
    in_file = open("dracula.txt","r")

    # Part 2
    # Loop over every line in Dracula, print each line out!
    for line in in_file:
        print(line)

    # Part 3
    # Actually, fix that for loop... only print out the line if it has the word vampire in it!
    for line in in_file:
        if "vampire" in line:
            print(line)

    # Part 4
    # If you didn't already, make sure it prints the line no matter what case vampire is!
    for line in in_file:
        if "vampire" in line.lower():
            print(line)

    # Part 5
    # Count that up! How many lines contain the word vampire?
    count = 0
    for line in in_file:
        if "vampire" in line.lower():
            count += 1
    print("The vampire count is: " + str(count))

    # Part 6
    # Take the lines from Dracula that have vampire in it and write them to a second file named vampytimes.txt.
    count = 1
    with open("dracula.txt","r") as in_file:
        with open("vampytimes.txt","w") as vampire_lines:
            for line in in_file:
                if "vampire" in line.lower():
                    print("Wrote Vampire line: " + str(count) +  " " + line)
                    vampire_lines.write(line)
                    count += 1
    print("The vampire line count is: " + str(count -1))    
    in_file.close()

if __name__ == "__main__":
    main()
