from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string

im = Image.open(sys.argv[1]).convert('RGB')
arr = im.tobytes() #bytes(p.tobytes())
result = "CBCencrypt.png"
encrypt = b""
arrBlock = ''
key_stream = ''
padding = 16 - len(arr) % 16
arr += bytes(padding * ".".encode('utf8'))
iv =  bytes('abdfdsaasdfddijk'.encode('utf8'))
key = 16 * 'a'
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
for i in range(int(len(arr)/16)):
    arrBlock=arr[i*16:i*16+16]
    key_stream = bytes([a ^ b for a,b in zip(arrBlock, iv)])
    iv = key_stream
    encrypt += cipher.encrypt(key_stream)
    #print(key_stream)
encrypt = encrypt[:-padding]
s = Image.frombytes("RGB",im.size,bytes(encrypt))
s.save(result, "png")
s.show()



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