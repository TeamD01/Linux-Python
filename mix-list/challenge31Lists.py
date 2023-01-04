#!/usr/bin/env python3
""" Alta3 Research | Lists Challenge """

# import random module
import random

def main():
    
    # enter variable data
    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 
            'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 
            'Xiuxiang', 'Yaping']

    ''' 
        Part 3: Add a line of code that appends the integer 4 to the list wordbank.
    '''
    wordbank.append(4)
    
    '''
       Part 4 + Bonus: The list of TLG students for the course is consistently changing. 
    '''
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)}: "))-1
    name = tlgstudents[num]
    
    print(name + " always uses " +  str(wordbank[2]) + " " + wordbank[1] + " to indent.")
    
    name = random.choice(tlgstudents)
    print("Randomized: " + name)

if __name__ == "__main__":
    main()

