'''Challenge 28
    Time for something different- instead of writing code, we'll be repairing it. 
    The code block below uses all the concepts we learned about so far- lists, dictionaries, methods, 
    built-in functions, and concatenation!

    Create a new file!

        student@bchd:~$ vim tuesdaychallenge.py

    #!/usr/env/python3

    mylist= [1,2,3,4,5, "Python"]

    name= input(What is your name?\n>)

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!
print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")

As you make changes to fix the script, continue to execute the script to test it. 
For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. 
The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.
'''
#!/usr/env/python3

mylist= [1,2,3,4,5, "Python"]

name= input("What is your name?\n>")  # changed line--see below

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!
#print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
print("Hi " + name.upper() + "! Welcome to Day " + str(mylist[1]) + " of " + mylist[5] + " Training!")

'''Run #1 error: 
    File "/home/student/mycode/challenges/challenge28.py", line 28
    name= input(What is your name?\n>)
                ^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?

Change: What is your name?\n>  to  "What is your name?\n>"
'''

'''Run #2 error:
    File "/home/student/mycode/challenges/challenge28.py", line 32
    print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
Change print line to: 
print("Hi " + name.upper() + "! Welcome to Day " + str(mylist[1]) + " of " + mylist[5] + " Training!")
'''

