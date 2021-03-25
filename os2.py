#!/usr/bin/env python3

# From geeksforgeeks.org/os-module-python-examples

# Using current working directory  
# search for all commands with "cwd"

# Imports
import os

# Constants
FILE = "/tmp/cwd"

f = open(FILE, "w")
f.write("dir(os)")
