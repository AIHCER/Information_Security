import sys

def encryptCaeser(key, plaintext):
    result=''
    for i in range (len(plaintext)):
        tempInt = ord(plaintext[i])+ord(key)-48
        if (tempInt > 122):
            tempInt -= 58
        else:
            tempInt -= 32
        result += chr(tempInt)
    return result

cipher = sys.argv[1]
key = sys.argv[2]
plaintext = sys.argv[3]
print (encryptCaeser(key, plaintext))
