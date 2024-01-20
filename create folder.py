import os
from datetime import datetime

now = datetime.now()
month = now.month
year = now.year
day = now.day

def create_folder():
    path = "./" + str(year) + "_" + str(month) + "_" + str(day)

    try:
        os.mkdir(path)
        print("Folder %s created!" % path)
    except FileExistsError:
        print("Folder %s already exists" % path)
