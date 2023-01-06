#!/usr/bin/env python

# Module Import Challenge

''' 
Python's popularity comes from the fact that it had a REDONKULOUS library of pre-written code that saves 
you the time/effort/skill of writing it yourself! The Python library is like a Swiss army knife- a tool 
for every occasion!

Below is a dictionary taken from the Open Trivia Database. What's annoying about this resource is that 
much of the data it returns is in HTML format (those weird &#039; characters you see below).

FORTUNATELY, there's a tool for that! The html module can clean that up for us. 
You'll need the documentation in the link below to solve the challenge.
'''

'''
Objective:
create a script that includes the trivia dictionary below.
Slice and print out the trivia question and the four answers (one correct, three incorrect) from the dictionary.
Use the html library to render the question/answers in the proper format.
BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly!
'''

def main():
    
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question= trivia["question"]

correct= trivia["correct_answer"]
incorrect1= trivia["incorrect_answers"][0]
incorrect2= trivia["incorrect_answers"][1]
incorrect3= trivia["incorrect_answers"][2]



