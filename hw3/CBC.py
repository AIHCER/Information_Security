from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string


ppm = ("./myppm.ppm")
im = Image.open('./1200px-NewTux.svg.png').convert('RGB')
p = Image.open(ppm)
key = 16 * 'a'
arr = bytes(p.tobytes())
print (len(arr))
encrypt = ""
arrBlock = ''
key_stream = ''
padding = 16 - len(arr) % 16
arr += bytes(padding * ".".encode('utf8'))
iv = 16* 'a'
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
#iv = ''.join(random.choice(letters) for i in range (16))
for i in range(int(len(arr)/16)):
    i = int(len(arr)/16) - 1 
    for j in range(16):
        arrBlock += chr(arr[i*16 + j])
    key_stream_list = [ord(a) ^ ord(b) for a,b in zip(arrBlock, iv)]
    for i in (key_stream_list):
        key_stream += chr(i)
    tempList = cipher.encrypt(key_stream.encode('utf8'))
    for i in range(len(tempList)):
        encrypt += chr(tempList[i])
    print(key_stream)
    key_stream = ''
encrypt = encrypt[:-padding]
Image.frombytes("RGB",p.size,encrypt,"raw","RGB").save(ppm)


#plaintext2 = ''
#print(key_stream_list)

#print(key_stream)
#ciphertext = cipher.encrypt(key_stream.encode("utf8"))
#print(ciphertext)
#
#
#before_iv = cipher.decrypt(ciphertext)
#for i in range(len(before_iv)):
#    plaintext2 += (chr(before_iv[i] ^ ord(iv[i])))
#print(plaintext2)