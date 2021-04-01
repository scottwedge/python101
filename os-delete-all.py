#!/usr/bin/env python3

# Script to delete all contents under a directory
# Get to base of directory and delete from there upwards

# Imports 
import os

# Constants
BASE = "/tmp/tmp"


# Functions
def work_down(dir):     # work down to bottom-most directory or file
    os.chdir(dir)    # assume directory exists
    contents = os.listdir()
    for j in contents:
        if os.path.isfile(j):
            delete_file(j)   # delete all files in directory
    contents = os.listdir()  # new listing of contents (only directories)
    for j in contents:
        if os.path.isdir(j):
            os.chdir(os.getcwd() + "/" + j)
   

def delete_file(f):   # delete file
    os.remove(f)


# Start at BASE directory
if os.path.exists(BASE) == False:    # Check that it exists
    print("Base directory {} does not exist!".format(BASE))
else:
    os.chdir(BASE)
    work_down(BASE)
