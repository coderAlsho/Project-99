import time
import os
import shutil
import datetime

x = datetime.datetime.now()
datadir = os.path("/Users/mac/Desktop/Project 97/Sample1.txt")
NumOfDays = time.time()

isExist = os.path.exists(datadir)

if(isExist == 'true'):
    os.walk(datadir)
    os.path.join(datadir)

    Ctime = os.stat(datadir).st_ctime