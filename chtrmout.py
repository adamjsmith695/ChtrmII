import time
import os

curLn = 0
    
#_________________________________________________________________

chtLog = open("chtLog.txt","r+")
line = ("")

#_________________________________________________________________

def clrcht(cht):
    time.sleep(0.1)
    cht.truncate(0)
    cht.seek(0)
    cht.flush()
    os.fsync(cht)
        
#_________________________________________________________________

while True:

    line = chtLog.readline()
        
    if curLn != 0:
        for x in range(0,curLn):
            line = chtLog.readline()

    #print(curLn)
            
    if line == "[CLEAR LOG]":
        curLn = 0
        print(" <<CONSOLE>> Please wait 2 seconds for log to clear ...\n")
        clrcht(chtLog)
        time.sleep(2)
            
    elif line != "":
        curLn += 1
        print(line)
        #clrcht()
    chtLog.seek(0)
    time.sleep(0.1)
