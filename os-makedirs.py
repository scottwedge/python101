#!/usr/bin/env python3

# Fooling around with os.makedirs()
# Create a long string of sub-directories
# need to use mode of "0oxxx" instead of "xxx" according to help

# Imports
import os
import random
import string

# under "/tmp/tmp/" create long directories path

# Constants
BASE = "/tmp/tmp"  # base directory
MODE = 0x755
MAX_NUM = 9999
MAX_DIR_DEPTH = 3

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

full_alphabet = lower_alphabet + upper_alphabet
old_name = BASE

for k in range(MAX_DIR_DEPTH):
    # Create directory name of random length of random alphabet characters
    random_length = random.randint(1,10)
    new_name = ""  # initialize name 
    for j in range(random_length):
        index = random.randint(0, len(full_alphabet) - 1)
        new_name = new_name + list(full_alphabet)[index]
    
    # Then append random number to directory name
    new_name = new_name + str(random.randint(0,MAX_NUM))
    
    full_path = os.path.join(old_name, new_name)
    old_name = full_path

print("NEW FULL PATH=", full_path)
os.makedirs(full_path, MODE)   # create new directory
