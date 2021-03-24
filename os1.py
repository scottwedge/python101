import os


max = 1000
for j in range(max):
    if not os.path.exists("/tmp/tmp"):
        os.mkdir("/tmp/tmp", mode=755)

    # create subdirectory
    f = open("/tmp/tmp/tmp" + str(j), "w")
    f.close()
