from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string

im = Image.open(sys.argv[1]).convert('RGB')
key = 16 * 'a'
arr = im.tobytes()
result = "CBCdecrypt.png"
plaintext = b""
arrBlock = ""
key_stream = ''
padding = (16 - len(arr) % 16) % 16
arr += bytes(padding * ".".encode('utf8'))
iv = bytes(16* 'a'.encode('utf8'))
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
#iv = ''.join(random.choice(letters) for i in range (16))
for i in range(int(len(arr)/16)):
    arrBlock = arr[i*16:i*16+16]
    tempList = cipher.decrypt(arrBlock)
    plain_part = bytes([a ^ b for a,b in zip(tempList, iv)])
    iv = tempList
    plaintext += plain_part
plain_part = plaintext[:-padding]
s = Image.frombytes("RGB",im.size,bytes(plaintext))
s.save(result, "png")
s.show()

