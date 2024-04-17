import random

message = input('text to encrypt: ')

def clean_text(t):

    t = ''.join(c for c in t if c.isalnum())
    t = t.lower()
    t = ''.join(t)
    return t

text = clean_text(message)

def generatekey(message):

    key = ""
    alphabet = list("abcdefghijklmnopqrstuvwyxz")
    
    for letter in range(0, len(message)):
        key = key + random.choice(alphabet)

    return key

key = generatekey(text)

print ("Key: " + key)

def encrypt(message, key):
    
    encryptq = ""

    for character, letter in zip(message, key):

        J = ord(character) + ord(letter)
        encryptq += chr(J)

    return encryptq

encryptq = encrypt(text, key)

print("Encrypted: " + encryptq)

def decrypt(encryptedm, key):

    decrypted = ""

    for character, letter in zip(encryptedm, key):

        J = ord(character) - ord(letter)

        decrypted += chr(J)

    return decrypted

encryptText = input("Enter Encrypted Message: ")
keyText = input("Enter key: ")

decrypted = decrypt(encryptText, keyText)

print("Decrypted: " + decrypted)

