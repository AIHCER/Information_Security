from Crypto.Cipher import AES
from PIL import Image
from Crypto import Random

def encrypt_guy(image,key):
    arr = bytes(image.tobytes())
    encrypt = ""
    arrBlock = []
    padding = 16 - len(arr) % 16
    arr += bytes(padding * ".")
    aes = AES.new(key,AES.MODE_ECB)
    for i in range(len(arr)/16):
        arrBlock.append(arr[i*16:(i+1)*16])
    for i in range(len(arr)/16):
        encrypt += aes.encrypt(arrBlock[i])
    encrypt = encrypt[:-padding]
    return Image.frombytes("RGB",image.size,encrypt,"raw","RGB")
if __name__ == "__main__":
    ppm = ("./myppm.ppm")
    im = Image.open('./guy.png').convert('RGB')
    im.save(ppm)
    p = Image.open(ppm)
    key = Random.new().read(AES.key_size[0])
    encrypt_guy(p,key).save(ppm)