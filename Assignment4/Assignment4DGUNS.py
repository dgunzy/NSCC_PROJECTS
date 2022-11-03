#!/usr/bin/python3
import sqlite3
from sqlite3 import Error

import assign4functions as sq 
#  Author: Daniel Guns
#  Date: Oct 26 2022
#  Class: Prog 1700
#  Database Assignment

def main():
    conn = sq.create_connection(r"assignment4database.db")
    ###This creates the connection and forms the database if it does not exist
    sq.create_projects_table(conn)
    ###this creates the project table if it does not exist
    sq.create_tasks_table(conn)
    ### this creates the tasks table if it does not exist
    
    userinput = 0
    print(            "Welcome to the Project Manager!")
    

    while userinput != 'q':
        ###this will loop through the various inputs unless the user hits 'q'
        userinput = input("\n     Press 1 see all projects: \n     Press 2 see all tasks: \n     Press 3 to create a new project: \n     Press 4 to create a new task: \n     Press 5 to delete a project: \n     Press 6 to delete a task:\n     Press q to quit:\n\nEnter your input here: ").strip()
        ###all the descriptions for these functions can be found in assign4functions.py
        if userinput == '1':
            try:
                sq.select_all_projects(conn)
            except:
                print("\nError: you must have entered somthing wrong!")
        elif userinput == '2':     
            try:
                sq.select_all_tasks(conn)
            except:
                print("\nError: you must have entered somthing wrong!") 
        elif userinput == '3':
            try:
                sq.create_new_project(conn)
            except:
                print("\nError: you must have entered somthing wrong!") 
        elif userinput == '4':
            try:
                sq.create_new_task(conn)
            except:
                ### this is a specific error message as some of the fields need to be integers
                print("\nError: you must have entered somthing wrong! \n Fields 1, 3, 4 need to be Integers!\n")  
        elif userinput == '5':
            try:
                sq.delete_a_project(conn)
            except:
                print("\nError: you must have entered somthing wrong!")  
        elif userinput == '6':
            try:
                sq.delete_a_task(conn)
            except:
                print("\nError: you must have entered somthing wrong!")
        elif userinput == 'q':
            break
        else:
            print("\nThat is not a recognized Input")

    sq.close_connection()
    ###this makes sure the connection closes after the user is finished

    print("\nThanks for using this Project Manager!")
main()
###this calles the main logic of the program
