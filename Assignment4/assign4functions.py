#!/usr/bin/python3

import sqlite3
from sqlite3 import Error

#  Author: Daniel Guns
#  Date: Oct 26 2022
#  Class: Prog 1700
#  Database Assignment
userinput = 0
def create_connection(db_file):
    """create a database connection to the sqlite database
    specified by db_file 
    :param db_file:database file
    :return: Connectoion object or None
    """
    ###this creats the database if it does nto exist
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    param create_table_sql: a CREATE TABLE statement
    :return"""
    ###This is the function to create a table in the database
    ###Used for both creating the project and task table
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def create_projects_table(conn):
    ### THis creates the projects table if it doesnt exist

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                         id integer PRIMARY KEY,
                                         name text NOT NULL,                                        begin_date text,
                                         end_date text
                                        ); """
    

    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print("\nError! Cannot create database connection.")

def create_tasks_table(conn):
    ###This creates the task table if it doesnt exist
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                 id integer PRIMARY KEY,
                                 name text NOT NULL,
                                 priority integer,
                                 status_id integer NOT NULL,
                                 project_id integer NOT NULL,
                                 begin_date text NOT NULL,
                                 end_date text NOT NULL,
                                 FOREIGN KEY (project_id) REFERENCES projects (id)
                             );"""
    

    if conn is not None:
        create_table(conn, sql_create_tasks_table)
    else:
        print("\nError! Cannot create database connection.")

def select_all_projects(conn):
    ###This function Selects the projects from the database to display them
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()
    ###this takes the column values and prints them
    data = cur.execute("""SELECT * FROM projects""")
    listofprojects = []
    for column in data.description:
        listofprojects.append(column[0])
    print(*listofprojects, sep= " - ")
    print("")
    
    for row in rows:
        print(row)


def select_all_tasks(conn):
    ###this function selects the tasks and displayes them
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    ### this takes the column values and prints them
    data = cur.execute("""SELECT * FROM tasks""")
    listoftasks = []
    for column in data.description:
        listoftasks.append(column[0])
    print(*listoftasks, sep = " - ")
    print("")
    for row in rows:
        print(row)

def create_new_project(conn):
    
    ###this function creates new projects by taking lines of input,
    ### and forming a list with them, and creating a tuple of the values
    with conn:
        projname = input("\nEnter the new project name: ")
        projdate1 = input("Enter the project start date(XXXX-XX-XX): ")
        projdate2 = input("Enter the project end date(XXXX-XX-XX): ")
        project = [projname, projdate1, projdate2]
        project = tuple(project)
    
        sql = '''INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?)'''

        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid



def create_new_task(conn):
    
    select_all_projects(conn)
    ###This function takes inputs, forms a list with them,
    ###Creates a tuple from the list, so it can be entered into the database
    with conn:
        
        tasknum3 = input("\nEnter project_id(int): ")
        taskname = input("Enter task name(): ")
        tasknum1 = input("Enter priorty number(1= Low 2 = Medium 3 = High): ")
        tasknum2 = input("Enter status_id(1= waiting 2 = In-Progress 3 = Done!): ")
        taskdate1 = input("Enter the task start date(XXXX-XX-XX): ")
        taskdate2 = input("Enter the task end date(XXXX-XX-XX): ")

        taskchange = [taskname, int(tasknum1), int(tasknum2), int(tasknum3), taskdate1, taskdate2]
        taskchange = tuple(taskchange)

        
        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                VALUES(?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, taskchange)
        conn.commit()

        return cur.lastrowid


def delete_a_project(conn):
    select_all_projects(conn)
    ###this function deletes a project from the list of projects
    
    projid = input("\nEnter the project number to delete: ")
    with conn:
       
        sql = 'DELETE FROM projects WHERE id = ?'
        cur = conn.cursor()
        cur.execute(sql, (projid,))
        conn.commit()




def delete_a_task(conn):
    select_all_tasks(conn)
    ### this function deletes a task from the list of tasks
    
    taskid = input("\nEnter the task number to delete: ")
    with conn:
      
        sql = 'DELETE FROM tasks WHERE id = ?'
        cur = conn.cursor()
        cur.execute(sql, (taskid,))
        conn.commit()


 
def close_connection():
    ###this function closes the connection to the database
    conn = None
    try:
        conn = sqlite3.connect(r"assignment4database.db")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
            print("\nConnection closed sucessfully")
  


