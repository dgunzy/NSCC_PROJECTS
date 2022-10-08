#!/usr/bin/python3

""" Author: Daniel Guns
 Date: Oct 6 2022
 Class: Prog 1700
 Dictionary Assignment"""



"""Think of a dictionary of at least 10 programming terms. Ask the user to input a term and show the definition as well as open the wikipedia article for the term.  If it is not know tell them and suggest some options to learn. remember firefox https etc 
Use the defenitions as values.  Lookup sleep function to open website later.
Print each word and its meaning seperately in a neat format.  Both the key and value need to have no quotes around them.  If it knows the term open a website - remember &!  If it doesnt know the term 
suggest some ottions.  
"""

import webbrowser
import time

progterms = {
    'function' : 'A block of code that only runs when it is called',
    'for loop' : 'A for loop repeats a segment of code a certain amount of times',
    'while loop' : 'A while loop will repeat a segment of code when the condition is true',
    'list' : 'A list is a way to store multiple items under one variable',
    'comment' : 'A comment in python is used to make notes or remarks in a block of code'
}
#enter all these
progwebsite = {
    'function' : 'https://en.wikipedia.org/wiki/Function_(computer_programming)',
    'for loop' : 'https://en.wikipedia.org/wiki/For_loop',
    'while loop' : 'A while loop will repeat a segment of code when the condition is true',
    'list' : 'A list is a way to store multiple items under one variable',
    'comment' : 'A comment in python is used to make notes or remarks in a block of code'
}

def countdown(x):
    while x > 0:
        time.sleep(1)
        x -= 1
        print(x)
        if x == 1:
            webbrowser.open(progwebsite[userguess], new=1)
            break



userguess = "start"
userguess = userguess.lower().strip()

# use print(" \t" to indent)
while userguess != "0":
    userguess = input(" Please enter the programming term you would like to look up! Enter 0 to quit:").lower().strip()
    if userguess == "0":
        break
    if userguess in progterms:
        print(userguess.title() + ":")
        print("\t" + progterms[userguess])
        time.sleep(2)
        print("Opening Website in:")
        countdown(4) 
        #webbrowser.open(progwebsite[userguess], new=1)

    elif userguess not in progterms:
        print("we dont have that try this instead")