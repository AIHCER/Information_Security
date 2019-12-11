import sys
import random
import math
def egcd(n,m):
    if m == 0:
        return 1,0
    else:
        x,y = egcd(m,n%m)
        x,y = y, (x - (n//m)*y)
        return x,y
def SaM(x,H,n):
    H = bin(H)[2:]
    val = 1
    for i in H:
        val = pow(val,2,n)
        #print(i)
        if(i == '1'):
            val = (val * x) % n
    return val

def randy(size):
    p = '1'
    for i in range(size-2):
        p += str(random.randint(0,1))
    p+= '1'
    return p
def MRtest(p):
    N = int(p,2)
    Nm1 = N-1
    k = 0
    m = Nm1
    while(m % 2 != 1):
        m = int(m / 2)
        k += 1
    for _ in range(0,5):
        a = random.randint(2,N-2)
        b = SaM(a,int(m),N)
        #b = pow(a,int(m)) % N
        if(b != 1 and b != Nm1):
            i = 1
            while(i<k and b != Nm1):
                b = SaM(b,2,N)
                #b = pow(b,2,N)
                if(b == 1):
                    return False
                i += 1
            if(b != Nm1):
                return False
    return True
def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)
instruc  = sys.argv[1]
if(instruc == 'init'):
    bitnum = int(sys.argv[2])
    if(bitnum < 2):
        print('bit too small')
        exit(0)
    elif(bitnum % 2 == 1):
        print('no odd number')
        exit(0)
    else:
        p = randy(int(bitnum/2))
        while(not MRtest(p)):
            #print('n')
            p = randy(int(bitnum/2))
            
        p = int(p,2)
        q = randy(int(bitnum/2))
        while(not MRtest(q)):
            q = randy(int(bitnum/2))
        q = int(q,2)  
        print(q)  
        n = p * q
        qo = (p-1) * (q-1)
        e = random.randint(2,qo-1)
        while(gcd(e,qo)!=1):
            e = random.randint(2,qo-1)
        d,y= egcd(e,qo)
        if(d<0):
            d += qo
        print('p =',p,'q =',q,'n =',n,'e =',e,'d =',d)
if(instruc == '-e'):
    plaintext = int(sys.argv[2].encode('utf-8').hex(),16)
    n = int(sys.argv[3])
    e = int(sys.argv[4])
    #encrypt = pow(plaintext,e) % n
    encrypt = SaM(plaintext,e,n)
    #print(plaintext)
    print(encrypt)
if(instruc == '-d'):
    ciphertext = int(sys.argv[2])
    n = int(sys.argv[3])
    d = int(sys.argv[4])
    decrypt = SaM(ciphertext,d,n)
    result = bytearray.fromhex(hex(decrypt)[2:-1]).decode()
    print(result)