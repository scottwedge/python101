#!/usr/bin/env python3

# Script to delete all files and directories unless they
# contain a file that starts with 'os'

# Imports
import os


# Constants
BASE = "/tmp/tmp"

# Move to starting directory (assumes it exists)
os.chdir(BASE)

# Verify at starting directory
j = os.getcwd()

if j == BASE:
    print("Starting at BASE", j)
else:
    print("Problem .. not starting at BASE", j)


