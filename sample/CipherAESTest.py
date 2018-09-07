import base64
import hashlib
import math
from Crypto import Random
from Crypto.Cipher import AES

#https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256

secret_key = 'this is secret:)this is secret:)'.encode()
message = 'Awesome python!!'.encode()
programtext = (r'input()' + "\r\n" + r'print("Hello World!")' + "\r\n").encode()


crypto = AES.new(secret_key.decode())


cipher_data2 = crypto.encrypt(programtext)
rom = (crypto.decrypt(cipher_data2)).decode()
print(rom)
exec(rom)








