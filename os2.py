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

print("functions with 'cwd' in them are: ", list_of_cwd)

f = open(FILE, "w")
f.write("List of functions in 'os' module:" + NEWLINE)
f.write(str(list_of_functions) + NEWLINE)
f.write("functions with 'cwd' in them are: " + NEWLINE)
f.write(str(list_of_cwd) + NEWLINE)
