#!/usr/bin/env python3

import os
import string
import random

max = 100000
print("MAX = {}".format(max))

alphabet = string.ascii_lowercase  # Create string of abc...xyz
print("Alphabet is: {}".format(alphabet))

if not os.path.exists("/tmp/tmp"):
    os.mkdir("/tmp/tmp", mode=755)

for j in range(max):
    random.seed()
    index = random.randint(0, len(alphabet) - 1)
    letter = list(alphabet)[index]
        
    index = random.randint(0, max)
    num = index
    
    f = open("/tmp/tmp/" + str(letter) + str(num), "w")   # create file
    f.close()  # close file
