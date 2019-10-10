import sys

def encryptCaeser(key, plaintext):
    result= ""
    for i in range (len(plaintext)):
        tempInt = ord(plaintext[i])+ord(key)-48
        if (tempInt > 122):
            tempInt -= 58
        else:
            tempInt -= 32
        result += chr(tempInt)
    return result.upper()

def encryptPlayfair(Key, plaintext):
    result = ""
    playfairSquare = []
    newkey = sorted(set(key), key = Key.index)
    for i in range (len(newkey)):
        if(newkey[i] == 'j'):
            print("!")
            newkey[i] = 'i'
    playfairSquare += newkey
    for i in range (ord('A'), ord('Z') + 1):
        if (chr(i) not in playfairSquare and chr(i) != 'J'):
            playfairSquare += chr(i) 
    plaintext = plaintext.upper()
    for i in range (len(plaintext)):
        if(i % 2 == 0):
            pairFirst = playfairSquare.index(plaintext[i])
            pairFirst_Row = pairFirst//5
            pairFirst_Column = pairFirst%5
            pairSecond = playfairSquare.index(plaintext[i+1])
            pairSecond_Row = pairSecond//5
            pairSecond_Column = pairSecond%5
            if(pairFirst_Row == pairSecond_Row):
                result += playfairSquare[(pairFirst//5) * 5 + (pairFirst + 1) % 5]
                result += playfairSquare[(pairSecond//5) * 5 + (pairSecond + 1) % 5]
            elif(pairFirst_Column == pairSecond_Column):
                result += playfairSquare[(pairFirst + 5) % 25]
                result += playfairSquare[(pairSecond + 5) % 25]
            else:
                result += playfairSquare[pairFirst_Row * 5 + pairSecond_Column]
                result += playfairSquare[pairSecond_Row * 5 + pairFirst_Column]
    return result.upper()

def encryptvernam(key, plaintext):
    result = ""
    key += plaintext
    for i in range (len(plaintext)):
        print(((ord(plaintext[i]) - 97) ^ (ord(key[i]) - 97)) + 65)
        result += chr(((ord(plaintext[i]) - 97) ^ (ord(key[i]) - 97)) + 65)
    return result.upper()


def encryptRow(key, plaintext):
    result = ""
    for i in range (len(key)):
        index = key.index(chr(i+49))
        for j in range(len(plaintext)):
            if (j % len(key) == index):
                result += plaintext[j]
    return result.upper()


def encryptRail(key, plaintext):
    result = ""
    lists = [[] for i in range(ord(key)-48)]
    length = (ord(key)-48) * 2 -2
    for i in range (len(plaintext)):
        upordown = i % length
        if(upordown < (ord(key)-49)):
            lists[upordown].append(plaintext[i])
        else:
            lists[length-upordown].append(plaintext[i])
    for i in range(ord(key)-48):
        for j in range (len(lists[i])):
            result += lists[i][j]
    return result.upper()



cipher = sys.argv[1]
key = sys.argv[2]
plaintext = sys.argv[3]
if (cipher == "caesar"):
    print (encryptCaeser(key, plaintext))
if (cipher == "playfair"):
    print (encryptPlayfair(key, plaintext))
if (cipher == "vernam"):
    print (encryptvernam(key, plaintext))
if (cipher == "row"):
    print (encryptRow(key, plaintext))
if (cipher == "rail_fence"):
    print (encryptRail(key, plaintext))

