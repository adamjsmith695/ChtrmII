from datetime import datetime
import time
from sys import argv
import pygetwindow

from censor import censor
win = pygetwindow.getActiveWindow()
win.size = (560, 125)
#____________________________________________________________________

print(chr(13))
chatActive = False
dtime = datetime.now()

chtrm = open("chtLog.txt","a")

#____________________________________________________________________

def clr():
    for x in range(1,25):
        print("\n\n")

#____________________________________________________________________

#usrnm = str(input("Enter a username : "))
#usernameu = str(usrnm.upper())
#username = sys.argv[1]
username = argv[1]

chtrm.write(str(" <<CONSOLE>> "+username+" has joined the room.\n"))
chtrm.flush()

time.sleep(1)
print("\nWelcome to the chatroom, "+(username)+"!")
time.sleep(1)
print("\nType '/help' and you will be\ngiven support and guidance.")
time.sleep(3)
clr()
chatActive = True

#____________________________________________________________________

while chatActive == True:
    inp = str(input("__________[Input]______________________________________________________\n\n >  "))
    clr()

    if inp == "/help":
        clr()
        time.sleep(0.2)
        print("This is a piece of chatroom software designed and created")
        print("by a fellow student. Don't mess around with it. Also keep")
        print("it somewhat lowkey as the teachers don't like anything even")
        print("potentially malicious, such as an under-the-table chatroom.")
        print("To use, type your inputs to the chat into this input console,")
        print("and by opening another IDLE output shell see yours and others'")
        print("chats together. Simple.")
        time.sleep(3)
        print("\nOther commands currently include:\n")
        time.sleep(0.5)
        print("'/date' - displays the date for you and everyone in the chatroom")
        time.sleep(0.5)
        print("'/quit' - shuts down this application. Also notifies the server \nthat you left, so please use this to close not the cross :)")
        input("\n\npress ENTER to continue")
        clr()
    elif inp == "/date":
        print("Date :",dtime.strftime("%d/%m/%y"))
        chtrm.write(str(" <<CONSOLE>> "+username+" requested the date: "+dtime.strftime("%d/%m/%y\n")))
        chtrm.flush()
        
        input("\n\npress ENTER to continue")
        clr()
    elif inp == "/quit":
        print("closing...")
        
        chtrm.write(str(" <<CONSOLE>> "+username+" has left the room.\n"))
        chtrm.flush()
        
        time.sleep(0.2)
        quit()
    elif inp == "/clearlog":
        chtrm.write(str("[CLEAR LOG]"))
        chtrm.flush()
    elif inp != "":
        
        if censor(inp) == True:
            censored = ("")
            for letter in inp:
                if letter != " ":
                    censored += ("#")
                else:
                    censored += letter
            inp = censored
        chtrm.write(str(" <"+username+"> "+inp+"\n"))
        chtrm.flush()

    
        
        
        
        
    
    
