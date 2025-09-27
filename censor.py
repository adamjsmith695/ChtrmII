
def format(msg,replace_symbols):
    newstr = ("")
    prevletter = ("")
    letterRepetition = 0

    if replace_symbols == True:

        for letter in msg.lower():
            if letter == '$' or letter == '5':
                msg = msg.replace(letter,'s')
            if letter == '£' or letter == '3':
                msg = msg.replace(letter,'e')
            if letter == '!' or letter == '1' or letter == '{' or letter == '}' or letter == '[' or letter == ']' or letter == '(' or letter == ')' or letter == '¦' or letter == '|':
                msg = msg.replace(letter,'i')
            if letter == '&' or letter == '@' or letter == '4':
                msg = msg.replace(letter,'a')
            if letter == '0':
                msg = msg.replace('0','o')
        #print(msg)

    for letter in msg.lower():            
        
        #print(ord(letter),letter)
        if ord(letter) >= 97 and ord(letter) <= 122:       #only allows letters and spaces to be added to th newstr var. -->
            if prevletter == letter:
                letterRepetition += 1       #this counts letter repeats, resetting to 0 if repetition stops.
            else:
                letterRepetition = 0

            if letterRepetition < 2:      #this allows the first 2 repeated characters to be added to newstr and excludes spaces.
                newstr += letter
                
            prevletter = letter         #this finalises by making the current letter now the previous letter for the next round.
            
            #print(newstr,"\n")
    #print(newstr)
    return newstr



def findMatch(msg, profanity, offset):
    
    countp = 0
    count = offset
    
    match = 0
    
    for y in range(len(profanity)):
        
        if len(profanity[y]) <= len(msg):
            
            for z in range(len(profanity[y])):
                
                countp += 1
                count += 1
                
                #print(profanity[y][countp],msg[count])
                
                if profanity[y][countp] == msg[count]:
                    #print("match")
                    match += 1
                    
                #print("countp =",countp,"\ncount =",count)
                #print("profanity =", profanity[y], "\nmsg =", msg)
                    
                if countp+1 == len(profanity[y]) or count+1 == len(msg):
                    
                    #if match+1 == len(profanity[y]):
                        #print("found profanity",profanity[y])
                        #return True
                    if (match+1)/(len(profanity[y])) >= 0.76: 
                        #print("found potential profanity",profanity[y])
                        return True
                    #print("next\n")
                    
                    count = offset
                    countp = 0
                    
                    match = 0
                    
                    break
                
                #print("\n")



#----------------------------------------CENSOR()----------------------------------------

    #this is the main function, formats string,
    #checks by letters in formatted string for profanities.
                

def censor(string):
    
    for x in range (0,2):       #this simply performs two different profanity checks
                                #with two different formats for a full profanity check.
        if x == 0:
            #print(0)
            msg = string
            msg = format(msg,False)     #format WITHOUT symbol replacements (,False)
        if x == 1:
            #print(1)
            msg = string
            msg = format(msg,True)      #format WITH symbol replacements (,True)
            
        #print(msg)
        profane = False         #just variable declaration


        
        for x in range(len(msg)-2):         #cycles through every letter of 'msg'; checks any that may include a profanity.
                                                                            #       |        
            if msg[x].lower() == "a":                                       #       V        
                profanity = ["ass", "arse","arrse","arsse","arrsse"]        #  for example, if the letter is 'a', it might preceed 'ass' or 'arse'. <---
                profane = findMatch(msg, profanity, x)                                                      #       |
                                                                                                            #       |
            elif msg[x].lower() == "b":                                                                     #       V
                profanity = ["btch","bitch","biitch","bittch","biittcch","biitcch","bittcch","bitcch"]      #  the odd character deviations simply ensures that any niche way of spelling it
                profane = findMatch(msg, profanity, x)                                                      #  is also detected - note that the format() function removes repeated characters                                                                                            #  after the second character (second character because some words in English include
                                                                                                #   This means all listed double repeated characters such as pa[ss] or l[oo]k). deviations covers 
                                                                                                #   all lengths of repeated characters, so e.g. 'biiiiiiiittttttch' under format() would become 
                                                                                                #   'biittch', which is listed and thus would be detected.
            elif msg[x].lower() == "c":                                                                     #       |
                profanity = ["cock","coock","cocck","coocck","cok","cunt","cnt","cuunnt","cuunt","cunnt"]   #       |
                profane = findMatch(msg, profanity, x)                                                      #       V
                                                                                                #same continues for the rest: _ _ _
            elif msg[x].lower() == "d":                                                         #                                  |
                profanity = ["dick","diick","dicck","diicck","dicc","diicc"]                    #                                  V 
                profane = findMatch(msg, profanity, x)

            elif msg[x].lower() == "f":
                profanity = ["fggt","faggot","fggot","fagot","faggoot","faagoot","faagot","faaggot","faaggoot","fuck","fck","fuuck","fucck","fuucck","fack","faack","facck","faacck","fock","foock","focck","foocck","feck","feeck","fecck","feecck","fucc","fuucc","facc","faacc","focc","foocc","fecc","fag","faag"]
                profane = findMatch(msg, profanity, x)

            elif msg[x].lower() == "n":
                profanity = ["nigger","niigger","niiger","niigeer","niiggeer","nigeer","niggeer","ngger","ngga","niggr","nigga","niigga","niiga","niga","nga"]
                profane = findMatch(msg, profanity, x)

            elif msg[x].lower() == "p":
                profanity = ["pussy","pusy","pssy","pussie","puussie","puussiie","pssiie","pssie","psiie","pssie","puusy","puussy","prick","prrick","prriick","prriicck","priicck","pricck","priick","prik","priik","prrik","prriik"]
                profane = findMatch(msg, profanity, x)

            elif msg[x].lower() == "r":
                profanity = ["retard","reetard","reettard","reettaard","reettaarrd","rettaarrd","reetaarrd","reettarrd","retaarrd","retarrd","rettarrd","rtrd","rttrd","rttrrd","rtrrd"]
                profane = findMatch(msg, profanity, x)
                
            elif msg[x].lower() == "s":
                profanity = ["shit","shhit","shhiit","shiit","sht","slut","sllut","sluut","slluut","slag","sllag","slaag","sllaag","shlag","shhlag","shhllag","shhllaag","shllaag","shlaag","shllag"]
                profane = findMatch(msg, profanity, x)
                
            elif msg[x].lower() == "t":
                profanity = ["twat","twwat","twaat","twwaat","tranny","trranny","trraanny","traanny","trany","trrany","trraany","traany"]
                profane = findMatch(msg, profanity, x)

            elif msg[x].lower() == "w":
                profanity = ["wank","waank","wannk","waannk","whore","whhore","whhoore","whhoore","whoore","whorre","whhorre","whhoorre","whhoorre","whoorre"]
                profane = findMatch(msg, profanity, x)


#find how to replace profanities with **** NOT DONE
#detect words based on structure, e.g. fyck can pass as not profane but f * ck will always represent fuck.
                
                
       
            if profane == True:     #returns true if a profanity is detected in
                return True         #the given input.







print(censor(input()))
