#!/usr/bin/env python3

# Script to delete all files and directories 
# (update later to not delete a directory or subdirectory
# if it contains a file that starts with a certain string)

# Imports
import os


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


base_list_of_file_or_dir = []  # initialize empty lists

still_deleting = True

if still_deleting:
    base_list_of_file_or_dir = os.listdir()
    if base_list_of_file_or_dir == []:  # Nothing left to delete
        still_deleting = False
    else:
        for j in base_list_of_file_or_dir:
            if os.path.isfile(j): # if is file then delete it
                os.remove(j)
                print("Just removed:", j)
            elif os.path.isdir(j): # if directory then go to it
                os.chdir(j)
                print("Just changed to directory", j)

print("DONE!")
