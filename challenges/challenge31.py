#!/usr/env/python3
import random

'''
EXERCISE: LISTS, INPUT, PRINT, VARIABLES

Objective: Add the following components to your code in this order:

PART 1. Put this list in your code:

wordbank= ["indentation", "spaces"] 
'''
wordbank = ["indentation", "spaces"]

'''
PART 2. Put this list in your code:
'''
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

'''
PART 3. Add a line of code that appends the integer 4 to the list wordbank.

'''
wordbank.append(4)

'''
PART 4. Include an input asking for a number between 0 and 20. Save this as the variable num.
'''


'''
PART 5. Remember that input() always returns a string... convert num into an integer!

PART 5. Use the integer num to slice one of the elements from the list tlgstudents. Save the name you return as the variable student_name.

PART 6. Using elements from the tlgstudents list and the student_name string, print this output.

<student_name> always uses <4> <spaces> to indent.
"4" and "spaces" should come from wordbank!

Bonus 1

Find a way to randomize what student name is picked. HINT: There is a function for this; don't be afraid to look for answers on the docs page!

Bonus 2

The list of TLG students for the course is consistently changing. Class sizes can expand or diminish with each teaching (although the expectation is that classes will grow!). Set the num variable to account for changing list lengths, without having to manually recode the list range. Finally, code the input() to allow the user to type a number beginning from 1 (users don't like to think about zero-indexing). Hint - Check the Python built-in functions.

'''


