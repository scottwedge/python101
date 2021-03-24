#!/usr/bin/env python3

import os
import string

max = 100
print("MAX = {}".format(max))

alphabet = string.ascii_lowercase  # Create string of abc...xyz
print("Alphabet is: {}".format(alphabet))

if not os.path.exists("/tmp/tmp"):
    os.mkdir("/tmp/tmp", mode=755)

for j in alphabet:
    for num in range(max):
        f = open("/tmp/tmp/tmp" + str(j) + str(num), "w")
        f.close()
