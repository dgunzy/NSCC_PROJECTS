#!/usr/bin/python3
import sqlite3
from sqlite3 import Error

import assign4functions as sq 
#  Author: Daniel Guns
#  Date: Oct 26 2022
#  Class: Prog 1700
#  Database Assignment

"""
1. view all projects
2. view all tasks
3. create new project
4. create new task
5. delete project
6. delete a task
7. quit the program
"""






# from sqlitefunctions import create_table
# from sqlitefunctions import create_project



"""create database table in called projects"""
conn = sq.create_connection(r"assignment4database.db")
sq.create_projects_table()
sq.create_tasks_table()

userinput = 0
print(            "Welcome to the Project Manager!\n")
while userinput != 'q':
    userinput = input("     Press 1 see all projects: \n     Press 2 see all tasks: \n     Press 3 to create a new project: \n     Press 4 to create a new task: \n     Press 5 to delete a project: \n     Press 6 to delete a task:\n     Press q to quit:" )
    if userinput == '1':
        try:
            sq.select_all_projects(conn)
        except:
            print("Error: you must have entered somthing wrong!")
    if userinput == '2':
        try:
            sq.select_all_tasks(conn)
        except:
            print("Error: you must have entered somthing wrong!")    
    if userinput == '3':
        try:
            sq.create_new_project()
        except:
            print("Error: you must have entered somthing wrong!")
    if userinput == '4':
        try:
            sq.create_new_task()
        except:
            print("Error: you must have entered somthing wrong! \n Fields 1, 3, 4 need to be Ints!\n")
    if userinput == '5':
        try:
            sq.delete_a_project()
        except:
            print("Error: you must have entered somthing wrong!")
    if userinput == '6':
        try:
            sq.delete_a_task()
        except:
            print("Error: you must have entered somthing wrong!")


print("\nThanks for using this Project Manager!")