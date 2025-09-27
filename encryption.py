import math

global offset
offset = 0          #change for encrypt/decrypt offset

def getKey():
    #gets the encryption key from certificate.txt - this key dictates
    #the result of the shuffle function, a different or incorrect key
    #is a different function for encryption/decryption and would not work.
    #Also deciphers the key.
    
    certificate = open("certificate.txt","r")
    public = certificate.readline()
    certificate.close()

    key = ("")
    
    for letter in public:
        letter = ord(letter)
    
        for x in range(0,32):
            y = letter * x
            while y > 255:
                y = y-223
            key += cipher(chr(y))
    return key


def cipher(string):
    #ciphers parameter string using a mathematical ciphering function.
    
    ciphered = ("")
    for letter in string:
        x = ord(letter)
        toRad = math.pi/180
        k = (255/90)
        y = abs(255*(math.sin((x/k)*toRad)))
        y = chr(math.floor(y))
        ciphered += y
    return ciphered

def decipher(string):
    #deciphers parameter string using the inverse of the mathematical
    #ciphering function.
    
    deciphered = ("")
    for letter in string:
        x = ord(letter)
        toDeg = 180/math.pi             
        k = (255/90)
        y = abs(k*((math.asin((x/255)))*toDeg))
        y = chr(math.ceil(y))
        deciphered += y
    return deciphered
        

def shuffle(string,key):
    #shuffles parameter string using the key retrieved from getKey()
    #function from certificate.txt
    
    shuffled = ("")
    for letter in string:
        x = ord(letter)
        global COUNTER
        if COUNTER > 255:
            COUNTER = 0

        global ADDER
        ADDER *= 2
        y = x+(ADDER*(ord((key[COUNTER]))))
        while y > 255:
            y = y-223
        if ADDER >= 128:
            ADDER = 2

        COUNTER += 1
        
        y = chr(y)
        shuffled += y
    return shuffled


def unshuffle(string,key):
    #unshuffles parameter string using the inverse function from the
    #shuffle function, using the key retrieved from getKey() function
    #from certificate.txt
    
    unshuffled = ("")
    for letter in string:
        x = ord(letter)
        global COUNTER
        if COUNTER > 255:
            COUNTER = 0
            
        global ADDER
        ADDER *= 2
        y = x-(ADDER*(ord((key[COUNTER]))))
        while y < 33:
            y = y+223
        if ADDER >= 128:
            ADDER = 2

        COUNTER += 1
        
        y = chr(y)
        unshuffled += y
    return unshuffled


def encrypt(string):
    #coordinates the functionality of key retrieval, ciphering and
    #shuffling functions to encrypt parameter string.
    
    global offset
    offset = abs(offset)
    key = getKey()
    global COUNTER
    COUNTER = 0 + offset
    global ADDER
    ADDER = 1 + offset
    string = cipher(string)
    string = shuffle(string,key)
    return string


def decrypt(string):
    #coordinates the functionality of key retrieval, deciphering and
    #unshuffling functions to decrypt parameter string.
    
    global offset
    offset = abs(offset)
    key = getKey()
    global COUNTER
    COUNTER = 0 + offset
    global ADDER
    ADDER = 1 + offset
    string = unshuffle(string,key)
    string = decipher(string)
    return string
