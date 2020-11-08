from Crypto.Cipher import AES
import hashlib

def padMessage(message):
    while (len(message) % 16 != 0):
        message += " "
    return message

def encryptString(message, password):
    password = password.encode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'dAfKMnokLPDKIsAr'
    paddedMessage = padMessage(message)
    cipher = AES.new(key, mode, IV)
    encryptMessage = cipher.encrypt(paddedMessage)
    return encryptMessage

def decryptString(message, password):
    password = password.encode()
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC
    IV = 'dAfKMnokLPDKIsAr'
    cipher = AES.new(key, mode, IV)
    decryptMessage = cipher.decrypt(message)
    decryptMessage = decryptMessage.rstrip().decode()
    return decryptMessage

# message = "Abril Vento"
# password = "secret"
# encryptedMessage = encryptString(message, password)
# print(encryptedMessage)
# decryptedMessage = decryptString(encryptedMessage, password)
# print(decryptedMessage)
