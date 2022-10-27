#!/usr/bin/python3

import sqlite3
from sqlite3 import Error

#  Author: Daniel Guns
#  Date: Oct 26 2022
#  Class: Prog 1700
#  Database Assignment

def create_connection(db_file):
    """create a database connection to the sqlite database
    specified by db_file 
    :param db_file:database file
    :return: Connectoion object or None
    """
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
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def create_projects_table():
    database = r"assignment4database.db"

    sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
                                         id integer PRIMARY KEY,
                                         name text NOT NULL,                                        begin_date text,
                                         end_date text
                                        ); """
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! Cannot create database connection.")

def create_tasks_table():
    database = r"assignment4database.db"

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
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! Cannot create database connection.")

def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return project id:
    """
    sql = '''INSERT INTO projects(name,begin_date,end_date)
            VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


def create_new_project():
    database = r"assignment4database.db"

    #create a database connection

    conn = create_connection(database)

    with conn:
        projname = input("\nEnter the new project name: ")
        projdate1 = input("Enter the project start date(XXXX-XX-XX): ")
        projdate2 = input("Enter the project end date(XXXX-XX-XX): ")
        project = [projname, projdate1, projdate2]
        project = tuple(project);
        # project = input("enter name date + date\n").split()
        # project = tuple(project);
        project_id = create_project(conn, project)


def create_new_task():
    database = r"assignment4database.db"

    #create a database connection

    conn = create_connection(database)
    select_all_projects(conn)
    with conn:
        
        tasknum3 = input("\nEnter project_id(int): ")
        taskname = input("Enter task name(): ")
        tasknum1 = input("Enter priorty number(1= Low 2 = Medium 3 = High): ")
        tasknum2 = input("Enter status_id(1= waiting 2 = In-Progress 3 = Done!): ")
        taskdate1 = input("Enter the task start date(XXXX-XX-XX): ")
        taskdate2 = input("Enter the task end date(XXXX-XX-XX): ")

        taskchange = [taskname, int(tasknum1), int(tasknum2), int(tasknum3), taskdate1, taskdate2]
        taskchange = tuple(taskchange)

        
        
        
        create_task(conn, taskchange)


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:
    :param id: id of the task:
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_project(conn, id):

    sql = 'DELETE FROM projects WHERE id = ?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_a_task():
    database = r"assignment4database.db"

    conn = create_connection(database)
    taskid = input("\nEnter the task number to delete: ")
    with conn:
       delete_task(conn, int(taskid))#;


def delete_a_project():
    database = r"assignment4database.db"

    conn = create_connection(database)
    projid = input("\nEnter the project number to delete: ")
    with conn:
       delete_project(conn, int(projid))#;



def select_all_tasks(conn):
    """
    Query all rows in the atasks table
    :param conn: The connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    print("ID# - TaskName - priority - status_id - project_id - begin_date - end_date ")
    for row in rows:
        print(row)


def select_all_projects(conn):
    """
    Query all rows in the atasks table
    :param conn: The connection object
    :return:
    """

    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()

    print("ID# - projname - begin_date - end_date ")
    for row in rows:
        
        print(row)