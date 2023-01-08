#!/usr/bin/env python
import html
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


# Objective:
# Create a script that includes the trivia dictionary below.
# Slice and print out the trivia question and the four answers (one correct, three incorrect) 
# from the dictionary.
# Use the html library to render the question/answers in the proper format.
# BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly!


def main():
    
    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": ["&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

    question = trivia["question"]
    print(question)

    correct = html.unescape(trivia["correct_answer"])
    print("A - " + correct)

    incorrect1 = html.unescape(trivia["incorrect_answers"][0])
    print("B - " + incorrect1)

    incorrect2 = html.unescape(trivia["incorrect_answers"][1])
    print("C - " + incorrect2)

    incorrect3 = html.unescape(trivia["incorrect_answers"][2])
    print("D - " + incorrect3)

    answer = input("Choose A, B, C, or D: ")
    if answer == "A":
        print("Nice job! You are correct.")
    else:
        print("Incorrect. " + correct + " is from the 1939 film Gone With the Wind. ")

if __name__ == "__main__":
    main()

