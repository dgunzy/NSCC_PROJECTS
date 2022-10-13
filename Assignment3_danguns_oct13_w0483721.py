#!/usr/bin/python3

""" Author: Daniel Guns
 Date: Oct 13 2022
 Class: Prog 1700
 Dictionary Assignment"""



"""Think of a dictionary of at least 10 programming terms. Ask the user to input a term and show the definition as well as open the wikipedia article for the term IF THEY HIT YES.  If it is not known tell them and suggest some options to learn.  
Use the defenitions as values.  Lookup sleep function to open website later.
Print each word and its meaning seperately in a neat format.  Both the key and value need to have no quotes around them.  If it knows the term open a website - remember &!  If it doesnt know the term 
suggest some options.  
"""

import webbrowser as wb #This imports the function to open a default webbrowser in python
import time   #This imports the ability to count down time 



#This is the main dictionary with the 10 terms and the definitions, it also has the key 'website' and the link to that website.
function = {'function' : '\n A block of code that only runs when it is called. A smaller block of code that can be re-used.', 'website': 'https://en.wikipedia.org/wiki/Function_(computer_programming)'}
for_loop = {'for loop' : '\n A for loop repeats a segment of code a certain amount of times.', 'website' : 'https://en.wikipedia.org/wiki/For_loop'}
while_loop = {'while loop' : '\n A while loop will repeat a segment of code when the condition is true.', 'website' : 'https://en.wikipedia.org/wiki/While_loop'}
my_list = {'list' : '\n A list is a way to store multiple items under one variable', 'website' : 'https://en.wikipedia.org/wiki/Linked_list'} 
comment = {'comment' : '\n A comment in python is used to make notes or remarks in a block of code that wont be read or acted on by the program.', 'website' : 'https://en.wikipedia.org/wiki/Comment_(computer_programming)'} 
data_type = {'data type' : '\n A data type is a set of values with rules for their operations, such as string or integer.', 'website' : 'https://en.wikipedia.org/wiki/Data_type'}
compiler = {'compiler' : '\n A program that translates a programming language to a target language, must be used for the "C" language.', 'website' : 'https://en.wikipedia.org/wiki/Compiler'}
variable = {'variable' : '\n A variable is a storage location for different data, such as strings, integers, and floats.', 'website' : 'https://en.wikipedia.org/wiki/Variable_(computer_science)'}
iterator = {'iterator' : '\n An iterator is an object that is used to navigate a container, like a list.', 'website' : 'https://en.wikipedia.org/wiki/Iterator'}
argument = {'argument' : '\n An argument, or a parameter is a variable used in a subroutine, like in the function add(x+y), the x and y are arguements.', 'website' : 'https://en.wikipedia.org/wiki/Parameter_(computer_programming)'}

terms_list = [function, for_loop, while_loop, my_list, comment, data_type, compiler, variable, iterator, argument]
#I stored the dictionaries in a list so they can be called easily, and it is more simple to add to it later if needed. 



#This is a function for the opening of the web browser and the countdown.
#I kept this seperate for clarity in the main block of code and to test the components individually. 

def webopen(countdown):
    while countdown > 0:
        time.sleep(1)
        countdown -= 1
        print(countdown, end="", flush=True)
        print(" ", end="", flush=True)
        if countdown == 1:
            if userguess in i:
                wb.open(i['website'], new=1 )
                break
#The while loop runs if the countdown variable is greater then 0, i used the imported time function to have the countdown work.  
#Each time it loops through it prints how many seconds are left and subtracts one from the total, countdown.
#When countdown hits 1 It opens the webbrowser using earlier for loop as the key for the terms_list list.


userguess = "start"
userguess = userguess.lower().strip()
print("Welcome to this Dictionary of Programming terms!")
print("Here are some terms you might be interested in:")
print("\n-Argument- -Comment- -Compiler- -Data Type- -For Loop-")
print("-Function- Iterator- -List- -Variable- -While Loop-")

#This is the main part of this program, it is contained in a while loop that keeps the dictionary running while the user does not guess 0.
#If the user guesses one of the terms in the dictionary, a for loop will run through the list of dictionaries,
#and the if statment will print the value if the input matches the key.  
#After the definition, the user can choose to type "yes" and this will use the if statement to call the function webopen().

while userguess != "0":
    userguess = input("\n Please enter the programming term you would like to look up! Enter 0 to quit:").lower().strip()
    if userguess == "0":
        break
    for i in terms_list:
        if userguess in i:
            print(userguess.title() + ":")
            print(i[userguess])
            print("")
            go_fwd = input("Type Yes to see a website about this topic, type No to look for a new term: ").lower().strip()
            if go_fwd == "yes":
                print("Opening Website in: ", end="",flush=True)
                webopen(4)
                break
            else:
                break
    
    # If the user's guess is not in the dictionary, this will print out some suggestions to try that will work.
    if  userguess not in i:
        print("Sorry we do not have that term in this Dictionary.")
        print("Here are some suggestions to try instead:")
        print("")
        print("-Argument- -Comment- -Compiler- -Data Type- -For Loop-")
        print("-Function- -Iterator- -List- -Variable- -While Loop-")
        

print("Thanks for using this programming terms Dictionary!!!")