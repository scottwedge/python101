#!/usr/bin/env python3

# Script to delete all files and directories 
# (update later to not delete a directory or subdirectory
# if it contains a file that starts with a certain string)

# Imports
import os


# Constants
BASE = "/tmp/tmp/tmp"

# Move to starting directory (assumes it exists)
os.chdir(BASE)

# Verify at starting directory
j = os.getcwd()

if j == BASE:
    print("Starting at BASE", j)
else:
    print("Problem .. not starting at BASE", j)


# Make a list of all absolute file paths in the directory
# by searching each for subdirectories and files
# Delete files from bottom of directory up
# if the filename does not begin with "os-"

list_of_file_or_dir = []  # initialize empty lists
list_to_remove = []
list_to_keep = []

file_or_dir = os.listdir()

for j in file_or_dir:
    if os.path.isfile(j) and 'os-' not in j: # if is most files, delete it
        #os.remove(j)
        list_to_remove.append(j)
    elif os.path.isfile(j) and 'os-' in j: # keep this file
        list_to_keep.append(j)
    elif os.path.isdir(j): # if directory then go to it
        os.chdir(j)
        p = os.cwd()

print("List of files to remove: ", list_to_remove)

