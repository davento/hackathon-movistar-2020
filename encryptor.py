from Crypto.Cipher import AES
import hashlib

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

# def encryptFile(file, password):
#     key = password.encode()
#     key = hashlib.sha256(key).digest()
#     mode = AES.MODE_CBC
#     cipher = AES.new(key, mode, IV)
#     with open(file, 'rb') as f:
#         originalFile = f.read()
#     padded_file = pad_message(originalFile)
#     encryted_message = cipher.encrypt(padded_file)
#     return encryptedMessage

# def decryptFile(file, password):
#     key = password.encode()
#     key = hashlib.sha256(key).digest()
#     mode = AES.MODE_CBC
#     cipher = AES.new(key, mode, IV)
#     with open(file, 'rb') as f:
#         encryptedFile = f.read()
#     decryptedFile = cipher.decrypt(encryptFile)

message = "Abril Vento"
password = "secret"
encrypted_message = encrypt_string(message, password)
print(encrypted_message)
decrypted_message = decrypt_string(encrypted_message, password)
print(decrypted_message)