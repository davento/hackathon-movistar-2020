from Crypto.Cipher import AES
import hashlib

IV = 'dAfKMnokLPDKIsAr'

def padMessage(message):
    while (len(message) % 16 != 0):
        message += " "
    return message

def padFile(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file

def encryptString(message, password):
    password = password.encode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    paddedMessage = padMessage(message)
    cipher = AES.new(key, mode, IV)
    encryptMessage = cipher.encrypt(paddedMessage)
    return encryptMessage

def decryptString(message, password):
    password = password.encode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    cipher = AES.new(key, mode, IV)
    decryptMessage = cipher.decrypt(message)
    decryptMessage = decryptMessage.rstrip().decode()
    return decryptMessage

def encryptFile(file, password):
    key = password.encode()
    key = hashlib.sha256(key).digest()
    mode = AES.MODE_CBC
    cipher = AES.new(key, mode, IV)
    with open(file, 'rb') as f:
        originalFile = f.read()
    padded_file = pad_message(originalFile)
    encryted_message = cipher.encrypt(padded_file)
    return encryptedMessage

def decryptFile(file, password):
    key = password.encode()
    key = hashlib.sha256(key).digest()
    mode = AES.MODE_CBC
    cipher = AES.new(key, mode, IV)
    with open(file, 'rb') as f:
        encryptedFile = f.read()
    decryptedFile = cipher.decrypt(encryptFile)

    



message = "Abril Vento"
password = "secret"
encryptedMessage = encryptString(message, password)
print(encryptedMessage)
decryptedMessage = decryptString(encryptedMessage, password)
print(decryptedMessage)