from os import listdir, chdir
from os.path import isfile, join
from operator import itemgetter, attrgetter, methodcaller
from shutil import copyfile
from pathlib import Path

mypath = ""

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
needfiles = []
for x in onlyfiles:
    if x == "smartmove.py":
        continue
    needfiles.append([x, int(x[:-4])])

result = sorted(needfiles, key=itemgetter(1))
print("files: ")
# print(sorted(needfiles, key=itemgetter(1)))
folder = 0
dividedby = 1500
new = dividedby
chdir(mypath)
for x in result:
    if new == dividedby:
        new = 0
        folder = folder + 1
        Path("dir"+str(folder)).mkdir(parents=True, exist_ok=True)
        print ("Switch to new folder " + "dir" + str(folder))
    copyfile(x[0], "dir"+str(folder) +"/" + x[0])
    print("Copyfile " + x[0], " to folder " + "dir"+str(folder) +"/" + x[0])
    new = new + 1
    