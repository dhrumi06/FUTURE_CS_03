from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = AES.block_size

def encrypt_file(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, BLOCK_SIZE))
    return cipher.iv + ct_bytes

def decrypt_file(enc_data, key):
    iv = enc_data[:BLOCK_SIZE]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(enc_data[BLOCK_SIZE:]), BLOCK_SIZE)
    return pt

