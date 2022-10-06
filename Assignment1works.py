#!/usr/bin/python3

""" Author: Daniel Guns
 Date: Sep 15 2022
 Class: Prog 1700
 The Case of Named users"""

username = input("Please enter your name here: ")

print("Your name in uppercase is " + username.upper().strip() + ". Your name in lowercase is " +
username.lower().strip() + ".  Your name in the proper form is " + username.title().strip() + ".")