from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string

im = Image.open(sys.argv[1]).convert('RGB') #用argv決定要加密的圖檔，並打開他
arr = im.tobytes()#把圖檔轉成bytes 
result = "CBCencrypt.png"#先開好output的圖檔
encrypt = b""
arrBlock = ''
key_stream = ''
padding = 16 - len(arr) % 16
arr += bytes(padding * ".".encode('utf8'))#決定要padding幾個'.'
iv =  bytes('aaaaaaaaaaaaaaaa'.encode('utf8'))#固定ivj
key = sys.argv[2] #從argv拿key
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
for i in range(int(len(arr)/16)):
    arrBlock=arr[i*16:i*16+16]#一次拿16個byte
    key_stream = bytes([a ^ b for a,b in zip(arrBlock, iv)])#先跟iv做XOR
    iv = key_stream
    encrypt += cipher.encrypt(key_stream)#再做加密
encrypt = encrypt[:-padding]#把剛剛padding的'.'拿掉
s = Image.frombytes("RGB",im.size,bytes(encrypt))
s.save(result, "png")#存檔
s.show()