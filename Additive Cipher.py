def encrypt(text, key):
    encrypted = ""
    for character in text:
        encrypted += chr((ord(character) + key - 65) % 26 + 65)
    return encrypted

def decrypt(cipher, key):
    decrypted = ""
    for character in cipher:
        decrypted += chr((ord(character) - key - 65) % 26 + 65)
    return decrypted

# text = "CRYPTO"
# key = 5

text = input("\nEnter the text to be encrypted: ")
key = int(input("Enter key: "))

encrypted = encrypt(text, key)
print("\nEncrypted: " + encrypted)
decrypted = decrypt(encrypted, key)
print("\nDecrypted: " + decrypted + "\n")