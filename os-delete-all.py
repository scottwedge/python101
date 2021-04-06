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
            print("Deleted file {} from {}".format(j, contents))
    contents = os.listdir()  # new listing of contents (only directories)
    for j in contents:
        if os.path.isdir(j):
            new_dir = os.path.join(os.getcwd(), j)
            work_down(new_dir)
            
def work_up(dir):
    os.chdir(dir)
    if os.listdir() == []:  # if directory is empty then go up and delete directory
        os.chdir("..")
        if os.getcwd() != BASE:
            os.removedirs(dir)

def delete_file(f):   # delete file
    os.remove(f)


def main():
    # Start at BASE directory and word down the subdirectories
    if os.path.exists(BASE) == False:    # Check that it exists
        print("Base directory {} does not exist!".format(BASE))
    else:
        os.chdir(BASE)
        list_dir = os.listdir()
        for j in list_dir:
            work_down(BASE)
    
            print("End up at {}".format(os.getcwd()))   #DEBUG
    
            # Now start working up the directory tree until get to the BASE
            # directory and delete empty directories along the way
    
            work_up(os.getcwd())


# Main code
if __name__ == "__main__":
    main()
