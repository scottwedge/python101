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
MAX = 9999

lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

full_alphabet = lower_alphabet + upper_alphabet
old_name = BASE

# Create directory name of random length of random alphabet characters
random_length = random.randint(1,10)
new_name = ""  # initialize name 
for j in range(random_length):
    index = random.randint(0, len(full_alphabet) - 1)
    new_name = new_name + list(full_alphabet)[index]

# Then append random number to directory name
new_name = new_name + str(random.randint(0,MAX))

full_path = os.path.join(old_name, new_name)
os.makedirs(full_path, MODE)
