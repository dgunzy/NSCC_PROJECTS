#!/usr/bin/python3

""" Author: Daniel Guns
 Date: Oct 6 2022
 Class: Prog 1700
 Dictionary Assignment"""



"""Think of a dictionary of at least 10 programming terms. Ask the user to input a term and show the definition as well as open the wikipedia article for the term.  If it is not known tell them and suggest some options to learn.  
Use the defenitions as values.  Lookup sleep function to open website later.
Print each word and its meaning seperately in a neat format.  Both the key and value need to have no quotes around them.  If it knows the term open a website - remember &!  If it doesnt know the term 
suggest some options.  
"""

import webbrowser #This imports the function to open a default webbrowser in python
import time   #This imports the ability to count down time 



#This is the main dictionary with the 10 terms and the definitions 
progterms = {
    'function' : 'A block of code that only runs when it is called. A smaller block of code that can be re-used.',
    'for loop' : 'A for loop repeats a segment of code a certain amount of times.',
    'while loop' : 'A while loop will repeat a segment of code when the condition is true.',
    'list' : 'A list is a way to store multiple items under one variable',
    'comment' : 'A comment in python is used to make notes or remarks in a block of code.',
    'data type' : 'A data type is a set of values with rules for their operations, such as string or integer.',
    'compiler' : 'A program that translates a programming language to a target language, must be used for the "C" language.',
    'variable' : 'A variable is a storage location for different data, such as strings, integers, and floats.',
    'iterator' : 'An iterator is an object that is used to navigate a container, like a list.',
    'argument' : 'An argument, or a parameter is a variable used in a subroutine, like in the function add(x+y), the x and y are arguements.'
}



#This is the dictionary I created that uses the same keys as the former one, mapped to the respective websites.
progwebsite = {
    'function' : 'https://en.wikipedia.org/wiki/Function_(computer_programming)',
    'for loop' : 'https://en.wikipedia.org/wiki/For_loop',
    'while loop' : 'https://en.wikipedia.org/wiki/While_loop',
    'list' : 'https://en.wikipedia.org/wiki/Linked_list',
    'comment' : 'https://en.wikipedia.org/wiki/Comment_(computer_programming)',
    'data type' : 'https://en.wikipedia.org/wiki/Data_type',
    'compiler' : 'https://en.wikipedia.org/wiki/Compiler',
    'variable' : 'https://en.wikipedia.org/wiki/Variable_(computer_science)',
    'iterator' : 'https://en.wikipedia.org/wiki/Iterator',
    'argument' : 'https://en.wikipedia.org/wiki/Parameter_(computer_programming)'

}
#This is a function for the opening of the web browser and the countdown.
#I kept this seperate for clarity in the main block of code and to test the components individually. 
def countdown(x):
    while x > 0:
        time.sleep(1)
        x -= 1
        print(x, end="", flush=True)
        print(" ", end="", flush=True)
        if x == 1:
            webbrowser.open(progwebsite[userguess], new=1 )
            break
#The while loop runs if the arguement x for the function is bigger then 0. 
#Each time it loops through it prints how many seconds are left and subtracts one from the total, x.
#When x hits 1 It opens the webbrowser using the Input as the key for the progwebsite dictionary.


userguess = "start"
userguess = userguess.lower().strip()

#This is the main part of this program, it is contained in a while loop that keeps the dictionary running while the user does not guess 0.
#If the user guesses one of the terms in the dictionary, I used an if statement to print the key value, 
#which is the definition of the term. 
#After the definition, I give the user 3 seconds to read it before the website countdown begins.
while userguess != "0":
    userguess = input(" Please enter the programming term you would like to look up! Enter 0 to quit:").lower().strip()
    if userguess == "0":
        break
    if userguess in progterms:
        print(userguess.title() + ":")
        print("\t" + progterms[userguess])
        time.sleep(3)
        print("Opening Website in: ", end="",flush=True)
        countdown(4) 
        
    #If the user's guess is not in the dictionary, this will print out some suggestions to try that will work.
    elif userguess not in progterms:
        print("Sorry we do not have that term in this Dictionary.")
        print("Here are some suggestions to try instead:")
        print("Argument, Comment, Compiler, Data Type, For Loop")
        print("Function, Iterator, List,  Variable, While Loop")

print("Thanks for using this programming terms Dictionary!!!")