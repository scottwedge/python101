#!/usr/bin/env python3

# Script to delete all files and directories 
# (update later to not delete a directory or subdirectory
# if it contains a file that starts with a certain string)

# Imports
import os

# Functions
def del_file_or_cd(cwd):
    os.chdir(cwd)
    list_file_or_dir = os.listdir()  # get list of contents of directory

    if list_file_or_dir == []:  # if directory empty
        full_path = os.getcwd()
        os.chdir("..") # move up one directory
        if full_path == BASE:
            pass
        else:
            os.remove(full_path)
    for j in list_file_or_dir:
        if os.path.isfile(j):
            os.remove(j)    # delete file
        elif os.path.isdir(j):
            os.chdir(j)
            del_file_or_cd(os.getcwd())  # call self

# Constants
BASE = "/tmp/tmp"

# Move to starting directory (assumes it exists)
os.chdir(BASE)

# Verify at starting directory
start_dir = os.getcwd()

if start_dir == BASE:
    print("Starting at BASE", start_dir)
else:
    print("Problem .. not starting at BASE", start_dir)

all_dir = []   # DEBUG

base_list_of_file_or_dir = os.listdir()   # initialize initial list of directory contents

for j in list(base_list_of_file_or_dir):

    if os.path.isfile(j): # if is file then delete it
        os.remove(j)
        print("Just removed:", j)
        continue  # return to next item in list
    elif os.path.isdir(j): # if directory then go to it
        os.chdir(j)
        print("Just changed to directory", j)
    else:   # other than file or directory
        pass   # what case could this be??

    # Now in new subdirectory
    print("Currently in directory: {}".format(os.getcwd()))   # DEBUG
    list_of_file_or_dir = os.listdir()    # DEBUG
    all_dir.append(list_of_file_or_dir)   # DEBUG
    print("Contains: {}".format(list_of_file_or_dir))   # DEBUG


print("All dir=", all_dir)
print("DONE!")
