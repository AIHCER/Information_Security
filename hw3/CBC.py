from Crypto.Cipher import AES
from PIL import Image
import sys
import random
import string

plaintext = 'abcdefghijklmnop'
iv = 16* 'a'
#iv = ''.join(random.choice(letters) for i in range (16))
key = 16 * 'a'
key_stream = ''
key_stream_list = [ord(a) ^ ord(b) for a,b in zip(plaintext, iv)]
plaintext2 = ''
print(key_stream_list)
for i in (key_stream_list):
    key_stream += chr(i)
print(key_stream)
cipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
ciphertext = cipher.encrypt(key_stream.encode("utf8"))
print(ciphertext)


before_iv = cipher.decrypt(ciphertext)
for i in range(len(before_iv)):
    plaintext2 += (chr(before_iv[i] ^ ord(iv[i])))
print(plaintext2)