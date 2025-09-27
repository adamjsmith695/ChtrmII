import time
from uuid import getnode as get_mac
import math
#import os
from subprocess import Popen, CREATE_NEW_CONSOLE
from encryption import encrypt, decrypt, offset

#------------------------------INITIALISATION------------------------------

def setUsername(newUser):
    #creates and stores an appropriately formatted new username
    #into _db__.txt
    
    if newUser == True:
        while True:
            time.sleep(0.1)
            username = input("<CONSOLE> Enter a Username.\n > ")
            db = open("_db__.txt","r",encoding="utf8")
            username = sanitise(username)

            if findUsername(username,db) == -1 and username != False:
                db = open("_db__.txt","r+",encoding="utf8")
                text = db.readline()
                text = decrypt(text)
                #text = decrypt(text)
                text = text.split(";")

                text[0] += ("," + username)
                text[1] += (", ")
                text[2] += ("," + getMac())

                encrypted = encrypt(text[0] + ";" + text[1] + ";" + text[2])

                db.truncate(0)
                db.seek(0)
                db.write(encrypted)
                db.close()
                 
                """
                db.seek((len(text[0])),0)
                db.write("," + username + ";" + text[1])
                db.seek((len(text[0]) + len(text[1]) +len(username))+2,0)
                db.write(", " + ";" + text[2])
                db.seek(len(text[0]) + len(text[1]) + (len(text[2]) + len(username))+5,0)
                db.write("," + getMac())
                db.close()
                """
                
                return username
            
            else:
                time.sleep(0.1)
                print("\n<CONSOLE> Sorry, that username already exists, or there was a problem with your input. Please try again.")
                time.sleep(4)
                print("\n\n")
    else:
        while True:
            time.sleep(0.5)
            
                


def getUsername(username):
    #returns, if existent, the index val of the given username, otherwise
    #returns -1
    
    db = open("_db__.txt","r",encoding="utf8")      
    return findUsername(username,db)
    

def setPassword(newUser):
    #creates and stores an appropriately formatted new password, linked to new username
    #into _db__.txt
    
    if newUser == True:
        while True:
            time.sleep(0.1)
            password = input("<CONSOLE> Enter a Password.\n > ")
            password = sanitise(password)

            if password != False:
                db = open("_db__.txt","r+",encoding="utf8")     
                text = db.readline()
                text = decrypt(text)
                #text = decrypt(text)
                text = text.split(";")

                text[1] = text[1][:-1]
                text[1] += (password)

                encrypted = encrypt(text[0] + ";" + text[1] + ";" + text[2])

                db.truncate(0)
                db.seek(0)
                db.write(encrypted)
                db.close()

                """
                db.seek(len(text[0])+len(text[1]) - 1,0)
                db.write("," + password)
                db.seek(len(text[0]) + len(text[1]) + len(password),0)
                db.write(";" + text[2])
                db.close()
                """
                
                return
            
   
def getPassword(username):
    #retrieves a password from _db__.txt that correlates to given
    #paramater username.
    
    db = open("_db__.txt","r",encoding="utf8")
    index = findUsername(username,db)
    if index != -1:
        db = open("_db__.txt","r",encoding="utf8")
        return findPassword(index,db)



def delay(x):
    #calculates the password delay for exceeding incorrect password attempts. More
    #exceeding of incorrect password attempts results in increasingly longer delays.
    
    delayMinutes = round(5**x)
    time.sleep(0.5)
    print("\n<CONSOLE> Credentials attempted incorrectly too many times.")
    time.sleep(2)
    print("<CONSOLE> Please wait",delayMinutes,"minute(s)...")
    time.sleep((delayMinutes*60))
    time.sleep(5)
    return x+1




def sanitise(string):
    #sanitises usrnm/pwd inputs given as parameter string. Returns False if unsanitary,
    #e.g. illegal characters are used or size is too large or small.
    #also automatically fills spaces with _'s and returns the string with _'s.
    
    if (len(string) < 3) or (len(string) > 12):
        return False
    
    sanitised = ("")
    
    for letter in string:
        if (ord(letter) < 32) or (ord(letter) > 126) or (ord(letter) == 44) or (ord(letter) == 59):   
            return False
        
        if ord(letter) == 32:
            sanitised += "_"
        else:
            sanitised += letter

    return sanitised



def findUsername(username,db):
    #Attempts to decrpyt, locate and return a given username's index in _db__.txt. Otherwise,
    #returns -1.
    
    usernames = db.readline()
    db.close()
    usernames = decrypt(usernames)
    db_array = usernames.split(";")
    usernames_array = db_array[0].split(",")
    
    for u in range(len(usernames_array)):
        if usernames_array[u] == username:
            return u
        
    return -1



def findPassword(index,db):
    #Attempts to decrpyt, locate and return a password from a given index in _db__.txt.
    #Should never return an index error as long as program is used as given; usernames
    #are saved along with a password always even if blank. The index parameter should
    #always be derived from findUsername(), as to always thus having a corresponding indexed
    #password (otherwise the return is already initially nullified).
    
    passwords = db.readline()
    db.close()
    passwords = decrypt(passwords)
    
    db_array = passwords.split(";")
    passwords_array = db_array[1].split(",")
    
    return passwords_array[index]




def login(createAccount):
    #coordinates the functions and UI for the creation of accounts and/or logging in,
    #including the coordination of incorrect password attempt wait timings.
    
    if createAccount == True:
        print("============================CREATE==ACCOUNT============================\n")

        username = setUsername(True)
        setPassword(True)

        cls()
        print("============================CREATE==ACCOUNT============================\n")
        time.sleep(0.1)
        print("<CONSOLE> Username =",username)
        time.sleep(0.1)
        print("<CONSOLE> Password =",asterisks(getPassword(username)),"\n\n")
        
        login(False)
        
    elif createAccount == False:
        incorrectAttempts = 0
        x = 0
        print("=================================LOGIN=================================\n")
        while True:
            time.sleep(0.1)
            username = input("<CONSOLE> Enter your username.\n > ")
            
            time.sleep(0.1)
            password = input("<CONSOLE> Enter your password.\n > ")

 
            if getUsername(username) != -1 and getPassword(username) == password:
                #start_chtrm()

                for y in range(0,3):
                    for x in range(0,4):

                        time.sleep(0.25)
                        
                        cls()
                        
                        if x == 0:
                            print("starting chtrmII")
                        elif x == 1:
                            print("starting chtrmII .")
                        elif x == 2:
                            print("starting chtrmII ..")
                        elif x == 3:
                            print("starting chtrmII ...")
                            
                        
                return username
            
                
            else:
                incorrectAttempts += 1
                if incorrectAttempts >= 5:
                    x = delay(x)
                    incorrectAttempts = 0
                else:
                    print("\n\n<CONSOLE> The username and/or password is incorrect.")
                    time.sleep(0.1)
                    print("<CONSOLE> You have",(5-incorrectAttempts),"more attempt(s).")
                    time.sleep(0.1)
                    print("<CONSOLE> Please try again...")
                    time.sleep(3)
                    print("\n")
        


def asterisks(string):
    asterisks = str("")
    for letter in string:
        asterisks += "*"
    return asterisks

def getMac():
    mac = get_mac()
    mac =':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    return mac

def findMac():
    db = open("_db__.txt","r",encoding="utf8")
    text = db.readline()
    text = decrypt(text)
    text = text.split(";")
    macAddresses = text[2].split(",")

    mac = getMac()
    for m in range(len(macAddresses)):
        if macAddresses[m] == mac:
            return m
    return -1

def cls():
    for x in range(5):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def initialiseLogin():
    print("Starting chtrm_II...")
    time.sleep(0.5)
    
    print("almost ready...")
    time.sleep(2)
    
    cls()

    choice = input("Press ⏎ to continue to login, or type / to create an account.\n")

    cls()
    
    if choice == "/":
        
        if findMac() != -1:
            
            print("============================CREATE==ACCOUNT============================\n")
            time.sleep(0.1)
            print("<CONSOLE> This device already has a registered account.")
            time.sleep(0.1)
            print("<CONSOLE> Please see the login page to log into your account.")
            time.sleep(4)
            print("\n\n")
            username = login(False)
            
        elif findMac() == -1:
            
            username = login(True)
        
    else:       
        username = login(False)

    return username



def launchChtrm(username):
    time.sleep(2)
    #os.system('chtrmin.py')

    Popen(["python", "chtrmout.py"], creationflags=CREATE_NEW_CONSOLE)
    time.sleep(0.5)
    Popen(["python", "chtrmin.py"] + [username], creationflags=CREATE_NEW_CONSOLE)
    
    #openIn()
    
    #import subprocess
    #subprocess.call(['python', 'chtrmin.py']) # Just run the program
    #input()
    #subprocess.check_output(['python', 'test.py']) # Also gets you the stdout



#------------------------------MAIN------------------------------


def Main():
    #print(encrypt("Adam;madA;D8:C4:97:BB:27:95"))
    #print(decrypt("c©þ°7èaS¿×··UTãöDD8æº{|®Ä¸ßÏDBW¸»_Ö~4XKõü9\<æy¬º)Öb#¹4ð´VYÊÀ¥ñ]ePèAoÈõ>)ÜØï.&³ÎC³~Áºð ÁTl}BÁÉFesb"))
    #input()
    #setUsername(True)
    #setPassword(True)
    
    launchChtrm(initialiseLogin())
    
    #username = "Adam"
    #launchChtrm(username)

        
Main()

#login("","",True)

#while True:
#    print(sanitise(input("\n > ")))





#NEED TO:

# - Modify the setPassword and setUsername system to operate consecutively immediately, otherwise
#   as username is saved after username prompt, there is a chance if program fails etc. only a username without
#   password is saved. Not ideal, room for manipulation, bugs etc.
#   note: temporary fix is in place; if no password is ever entered, password for that username remains as " ".

# - Modify Delay function. Needs to globally maintain a delay per MAC address, even outside of program runtime.
#   The whole mechanism is essentially pointless currently because a user can simply restart the program to avoid
#   the delay.

# - Check that findPassword() can deal with invalid inputs for index parameter, particularly a -1 input.s

# - Chtrm must open a new input window. This window is it's own subprocess - always available for inputting messages.
#   The current window/instance of python will become a receiver, displaying all messages from a text file. There should
#   be a public file that is put onto the shared area in a specific place. Each computer, whilst running the program, will
#   copy each message as they come onto the shared area file into a local text file. This allows for a build up of messages to
#   be printed, and localises the system as different computers will be in different states/positions.


