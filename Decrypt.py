import sys
if len(sys.argv) == 4:
    Cipher = sys.argv[1]
    Key = sys.argv[2]
    Ctext = sys.argv[3]

    if(Cipher == "caesar"):
        Ptext = ""
        k = int(Key)
        for i in Ctext:
            p = (ord(i) - ord('A') - k) % 26
            Ptext+= chr(p + 97)
        print(Ptext)
    elif(Cipher == "playfair"):
        rk = []
        Cset = set()
        ctable = [[0 for i in range(5)] for j in range(5)]
        for c in Key:
            if c == 'J':
                c = 'I'
            if c not in Cset:
                Cset.add(c)
                rk.append(c)
        
        for a in range(65,91):
            if chr(a) == 'J': #abandon letter J
                continue
            if chr(a) not in Cset:
                Cset.add(chr(a))
                rk.append(chr(a))
        
        for i in range(5):
            for j in range(5):
                ctable[i][j] = rk[(i * 5)+j]
        temp = ''
        substr = ''
        for c in Ctext:
            temp = c
            substr += c
        pair = []
        plaintext = ""
        for i in range(0,len(substr),2):
            pair.append(substr[i:i+2])
        for i in range(len(pair)):
            for a in range(5):
                for b in range(5):
                    if ctable[a][b] == pair[i][0]:
                        x1 = a
                        y1 = b
                    if ctable[a][b] == pair[i][1]:
                        x2 = a
                        y2 = b
            if(x1 == x2):
                plaintext += ctable[x1][(y1-1)%5] +ctable[x1][(y2-1)%5]
            elif(y1 == y2):
                plaintext += ctable[(x1-1)%5][y1] + ctable[(x2-1)%5][y1]
            else:
                plaintext += ctable[x1][y2] + ctable[x2][y1]
        print(plaintext)#記得切成小寫

    elif(Cipher == 'vernam'):
        binKey = []
        bintext = []
        PtextV = ''
        binP = []
        for k in Key:
            binKey.append(ord(k)-ord('A'))
        for c in Ctext:
            bintext.append(ord(c)-ord('A'))
        for i in range(len(Ctext)):
            if(i<len(Key)):
                PtextV += chr((binKey[i]^bintext[i])+65)
                binP.append(binKey[i]^bintext[i])
            else:
                binP.append(binP[i-len(Key)] ^ bintext[i])
                PtextV += chr((binP[i-len(Key)] ^ bintext[i])+65)
        print(PtextV)
    
    elif(Cipher == 'row'):
        keynum = []
        for k in Key:
            keynum.append(int(k))
        maxCol = len(keynum)
        maxRow = int(len(Ctext)/maxCol)
        Ptable = [[0 for j in range(maxCol)] for i in range(int(maxRow))]
        plaintextR = ""
        for j in range(len(keynum)):
            for i in range(maxRow):
               Ptable[i][j] = Ctext[i + maxRow* (keynum[j]-1)]
        for i in range(maxRow):
            for j in range(maxCol):
                plaintextR += Ptable[i][j]
                
        print(plaintextR)



                


        
        
else:
    print("Please follow the input rule")
