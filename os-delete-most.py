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

all_dir = []   # DEBUG

base_list_of_file_or_dir = os.listdir()   # initialize initial list of directory contents

for j in list(base_list_of_file_or_dir):

    still_deleting = True
    
    while still_deleting:
        if os.path.isfile(j): # if is file then delete it
            os.remove(j)
            print("Just removed:", j)
            still_deleting = False  # exit while loop
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

#        if list_of_file_or_dir == []:  # At lowest subdirectory, is empty
#            if os.getcwd() == BASE:
#                still_deleting = False
#            else:
#                os.chdir("..")   # move up one directory
#                contents = os.listdir()
#                os.rmdir(contents)

print("All dir=", all_dir)
print("DONE!")
