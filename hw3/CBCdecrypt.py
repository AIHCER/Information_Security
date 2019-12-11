from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string

im = Image.open(sys.argv[1]).convert('RGB')  #開檔
key = sys.argv[2] #從argv輸入key
arr = im.tobytes() #把圖轉成bytes
result = "CBCdecrypt.png" #先開好output的圖檔
plaintext = b""
arrBlock = ""
key_stream = ''
padding = (16 - len(arr) % 16) % 16#決定要padding幾個
arr += bytes(padding * ".".encode('utf8')) #padding
iv = bytes(16* 'a'.encode('utf8'))#固定iv
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
for i in range(int(len(arr)/16)):
    arrBlock = arr[i*16:i*16+16] #一定拿16個byte出來
    tempList = cipher.decrypt(arrBlock)
    plain_part = bytes([a ^ b for a,b in zip(tempList, iv)]) #上面那行先解密，這要再做XOR
    iv = tempList #把iv更新成XOR之前的那個stream，給下一次用
    plaintext += plain_part #把XOR好的結果加到明文的string裡面
plain_part = plaintext[:-padding]#去掉padding
s = Image.frombytes("RGB",im.size,bytes(plaintext))
s.save(result, "png")# 存檔
s.show()