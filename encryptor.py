from Crypto.Cipher import AES
import hashlib
import os

IV = 'dAfKMnokLPDKIsAr'

def pad_message(message):
    while (len(message) % 16 != 0):
        message += " "
    return message

def pad_file(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file

def cipher_object(password):
    key = password.encode()
    key = hashlib.sha256(key).digest()
    mode = AES.MODE_CBC
    cipher = AES.new(key, mode, IV)
    return cipher

def encrypt_string(message, password):
    padded_message = pad_message(message)
    cipher = cipher_object(password)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_string(message, password):
    cipher = cipher_object(password)
    decrypted_message = cipher.decrypt(message)
    decrypted_message = decrypted_message.rstrip().decode()
    return decrypted_message

def encrypt_file(file, password):
    cipher = cipher_object(password)
    with open(file, 'rb') as f:
        originalFile = f.read()
    padded_file = pad_file(originalFile)
    encrypted_file = cipher.encrypt(padded_file)
    with open(file, 'wb') as e:
        e.write(encrypted_file)

def decrypt_file(file, password):
    cipher = cipher_object(password)
    with open(file, 'rb') as f:
        encrypted_file = f.read()
    decrypted_file = cipher.decrypt(encrypted_file)
    with open(file, 'wb') as e:
        e.write(decrypted_file)

message = "Abril Vento"
password = "secret"
encrypted_message = encrypt_string(message, password)
print(encrypted_message)
decrypted_message = decrypt_string(encrypted_message, password)
print(decrypted_message)

file_name = "img.jpg"
super_pasword = "super secret"
encrypt_file(file_name, password)
encrypt_file(file_name, password)
decrypt_file(file_name, password)
decrypt_file(file_name, password)
