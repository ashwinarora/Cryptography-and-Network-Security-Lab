# C = (P * K1 + K2) % 26
# P = ((C - K2) x K1 ^ -1 ) % 26

def encrypt(text, key_1, key_2):
    encrypted = ""
    for character in text:
        encrypted += chr(((ord(character) - 65) * key_1 + key_2) % 26 + 65)
    return encrypted

def decrypt(text, key_1, key_2):
    decrypted = ""
    key_1 = mul_inv(key_1)
    for character in text:
        decrypted += chr((ord(character) - 65 - key_2) * key_1 % 26 + 65)
    return decrypted

def mul_inv(num):
    for i in range(0,26):
        flag = (num * i) % 26
        if flag == 1:
            return i

# text = "HELLO"
# key_1 = 7
# key_2 = 2

text = input("\nEnter the text to be encrypted: ")
key_1 = int(input("Enter key 1: "))
key_2 = int(input("Enter key 2: "))
encrypted = encrypt(text, key_1, key_2)
print("\nEncrypted: " + encrypted)
decrypted = decrypt(encrypted, key_1, key_2)
print("\nDecrypted: " + decrypted + "\n")