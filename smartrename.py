from os import listdir
from os.path import isfile, join, isdir
from os import chdir, rename
from operator import itemgetter, attrgetter, methodcaller
from shutil import copyfile
from pathlib import Path

mypath = ""

name = 1
onlydirs = [d for d in listdir(mypath) if isdir(join(mypath, d))]

print("dirs: ")
print(onlydirs)
folder = 0
dividedby = 1500

for x in onlydirs:
    print("Entering folder " + x + "...")
    chdir(join(mypath, x))
    curr_dir = join(mypath, x)
    onlyfiles = [f for f in listdir(curr_dir) if isfile(join(curr_dir, f))]
    for e in onlyfiles:
        print ("Rename file " + e + " to " + str(name) + ".jpg")
        rename(e, str(name) + ".jpg")
        name = name + 1
        #quit()
    print("Returning to up folder...")
    chdir("../")
    