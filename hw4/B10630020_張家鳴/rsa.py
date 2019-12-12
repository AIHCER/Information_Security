import sys
import random
import math

def randomPrime(bitsize):
    p = '1'
    for _ in range(bitsize - 2):
        p += str(random.randint(0, 1))
    p += '1'
    return p

def sam(x, H, n):
    H = bin(H)[2:]
    result = 1
    for i in H:
        result = pow(result, 2, n)
        if(i == '1'):
            result = (result * x) % n
    return result


def MRtest(p):
    p = int(p, 2)
    p_minus = p - 1
    k = 0
    m = p_minus
    while(m % 2 == 0):
        m = int(m / 2)
        k += 1
    for _ in range(0, 5):
        a = random.randint(2, p - 2)
        b = sam(a, int(m), p)
        if(b == 0 and b != p_minus):
            i = 1
            while(i < k and b != p_minus):
                b = sam(b, 2, p)
                if(b == 1):
                    return False
                i += 1
            if (b != p_minus):
                return False
    return True

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def egcd(a, b):
    if (b == 0):
        return 1, 0
    else:
        x, y = egcd(b, a % b)
        x, y = y, (x - (a // b) * y)
        return x, y

option = sys.argv[1]
if(option == 'init'):
    bitsize = int(sys.argv[2])
    print(bitsize)
    if((bitsize) < 2 or (bitsize % 2 != 0)): 
        print("invalid bit size")
        exit(0)
    else:
        p = randomPrime(int(bitsize/2))
        while(not MRtest(p)):
            p = randomPrime(int(bitsize/2))
        q = randomPrime(int(bitsize/2))
        while(not MRtest(q)):
            q = randomPrime(int(bitsize/2))
        p = int(p,2)
        q = int(q,2)
        n = p * q
        fi_q = (p-1) * (q-1)
        key_pub = random.randint(2, fi_q - 1)
        while(gcd(key_pub, fi_q) != 1):
            key_pub = random.randint(2, fi_q)
        key_pri, not_use = egcd(key_pub, fi_q)
        if(key_pri < 0):
            key_pri += fi_q
        
        print('p = ', p, 'q = ', q, 'n = ', n, 'public key = ', key_pub, 'private key = ', key_pri)

if(option == '-e'):
    plaintext = int(sys.argv[2].encode('utf-8').hex(),16)
    print(plaintext)
    n = int(sys.argv[3])
    key_pub = int(sys.argv[4])
    #encrypt = pow(plaintext,e) % n
    encrypt = sam(plaintext,key_pub,n)
    #print(plaintext)
    print(encrypt)
if(option == '-d'):
    ciphertext = int(sys.argv[2])
    n = int(sys.argv[3])
    key_pri = int(sys.argv[4])
    decrypt = sam(ciphertext,key_pri,n)
    result = bytearray.fromhex(hex(decrypt)[2:-1]).decode()
    print(result)   