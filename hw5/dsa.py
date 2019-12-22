import random
import binascii
import math
import hashlib
import sys

def self_xor(seed1, seed2):
    result = ''
    for _seed1, _seed2 in zip(seed1, seed2):
        if _seed1 == _seed2:
            result += '0'
        else:
            result += '1'
    return result
def self_or(x, y):
    _x = bin(x)
    _y = bin(y)
    for _ in range (0,len(_y) - len(_x)):
        _x = '0' + _x       
    result = ''
    for _x, _y in zip(_x, _y):
        if _x == '1' or _y == '1':
            result += '1'
        else:
            result += '0'
    return result
def MRtest(p):
    p_minus = p - 1
    k = 0
    m = p_minus
    while(m % 2 == 0):
        m //= 2
        k += 1
    for _ in range(0, 5):
        a = random.randint(2, p - 2)
        b = sam(a, int(m), p)
        if(b != 1 and b != p_minus):
            i = 1
            while(i < k and b != p_minus):
                b = sam(b, 2, p)
                if(b == 1):
                    return False
                i += 1
            if (b != p_minus):
                return False
    return True
def sam(x,H,n = -1):
    y = 1
    H = bin(H)[2:]
    for i in H:
        y = y * y
        if n != (-1):
            y = y % n
        if i == '1':
            y = y * x
            if n != (-1):
                y = y % n
        
    return y

def keygen():
    L = 1024
    n = 1023 // 160
    b = 1023 % 160

    while True:
        check = False
        q = 0
        seed = '1'
        while check == False:
            seed = '1'    
            for index in range (0,random.randrange(158, 512)):
                seed += str(random.randint(0, 1))
            seed += '1'
            g = len(seed)

            s = hashlib.sha1()
            s.update(seed)
            u1 = bin(int(binascii.hexlify(s.digest()), 16))[2:]
            
            s = hashlib.sha1()
            s.update(str((int(seed, 2) + 1) % sam(2, g)))
            u2 = bin(int(binascii.hexlify(s.digest()), 16))[2:]
            U = int(self_xor(u1, u2), 2)
            q = self_or(U, (sam(2, 159) + 1))
            q = int(q, 2)
            check = MRtest(q)
        
        counter = 0
        offset = 2

        while counter < 4096:
            w = 0
            i = 0
            v = []

            for k in range(0, n + 1):
                s = hashlib.sha1()
                s.update(str((int(seed,2) + offset + k) % sam(2, g)))
                v.append(int(binascii.hexlify(s.digest()), 16))
            
            for _v in v:
                if i != n:
                    w += _v * sam(2, i * 160)
                else:
                    w += (_v % sam(2,b)) * sam(2, i * 160)
                
                i += 1
            
            x = w + sam(2, L - 1)
            c = x % (2 * q)
            p = x - (c - 1)
            if p >= sam(2, L - 1):
                if MRtest(p):
                    return p,q
            print(counter)
            counter += 1
            offset =  offset + n + 1
            
options = sys.argv[1]

def abdgen(p, q):
    a = 1
    while a == 1:
        a = sam(random.randrange(2, p-2), (p-1)/q, p)
    d = random.randrange(0, q)
    b = sam(a, d, p)
    return a, b, d

if(options == 'gen'):
    p, q = keygen()
    a, b, d = abdgen(p, q)
    print (p, q)
    print ((p-1)%q)
    print (a, b, d)
    print (sam(a, q, p))
    # p, q, alpha, beta, d 都有了，剩的靠你big brain了