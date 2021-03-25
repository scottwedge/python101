#!/usr/bin/env python3

# From geeksforgeeks.org/os-module-python-examples

# Using current working directory  
# search for all commands with "cwd"

# Imports
import os

# Constants
FILE = "/tmp/cwd"
NEWLINE = "\n"

list_of_functions = dir(os)

print("List of functions in 'os' module:", list_of_functions)

list_of_cwd = []

for j in list_of_functions:
    if "cwd" in j:
        list_of_cwd.append(j)

print() # blank line
print("Functions with 'cwd' in them are: ", list_of_cwd)

f = open(FILE, "w")
f.writelines("List of functions in 'os' module:" + NEWLINE)
f.writelines(str(list_of_functions) + NEWLINE)
f.writelines(NEWLINE)
f.writelines("Functions with 'cwd' in them are: " + NEWLINE)
f.writelines(str(list_of_cwd) + NEWLINE)
