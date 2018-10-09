def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, columns):
            print(matrix[i][j], end='')
        print()

def getMatrix(key):
    alphabet = [-1] * 26
    matrix = [[-1] * 5 for _ in range(5)]
    column_count = 0
    row_count = 0
    for actual_character in key:
        effective_character = actual_character
        if(effective_character == 'J'): effective_character -= 1 #To convert 'J' into 'I'
        if (alphabet[ord(effective_character) - 65] == -1):
            alphabet[ord(effective_character) - 65] = column_count
            matrix[row_count][column_count] = effective_character
            column_count+=1
            if(column_count == 5):
                column_count = 0
                row_count+=1
    count = 0
    while (row_count < 5 and column_count < 5):
        while(alphabet[count] != -1):
            count+=1
            if(count == 9): count += 1
        alphabet[count] = column_count
        matrix[row_count][column_count] = chr(count + 65)
        column_count += 1
        if(column_count == 5):
            column_count = 0
            row_count+=1
    return matrix

def findInMatrix(matrix, item):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(0, rows):
        for j in range(0, columns):
            if(matrix[i][j] == item):
                return [i, j]

def operations(initial_string, key, shift):
    final_string = ""
    matrix = getMatrix(key)
    if(shift == 1): 
        print("\nThe matrix is:")
        print_matrix(matrix)
    pair = ['X', 'X']
    length = len(initial_string)
    jump = 2
    i = 0
    while(i < length):
        jump = 2
        pair[0] = initial_string[i]
        pair[1] = 'X'
        if(i != length - 1):
            pair[1] = initial_string[i+1]
            if (pair[0] == pair[1]):
                jump = 1
                pair[1] = 'X'
        loc_1 = findInMatrix(matrix, pair[0])
        loc_2 = findInMatrix(matrix, pair[1])
        if(loc_1[0] == loc_2[0]):
            final_string += matrix[loc_1[0]][(loc_1[1] + shift) % 5] + matrix[loc_2[0]][(loc_2[1] + shift) % 5]
        elif(loc_1[1] == loc_2[1]):
            final_string += matrix[(loc_1[0] + shift) % 5][loc_1[1]] + matrix[(loc_2[0] + shift) % 5][loc_2[1]]
        else:
            final_string += matrix[loc_1[0]][loc_2[1]] + matrix[loc_2[0]][loc_1[1]]
        i += jump
    return final_string

def encrypt(text, key):
    cipher = operations(text, key, 1)    
    return cipher

def decrypt(cipher, key):
    result = operations(cipher, key, -1)
    text = result[0]
    length = len(result)
    for i in range(1, length-1):
        if(result[i] != 'X' and result[i-1] != result[i+1]):
            text += result[i]
    if(result[length - 1] != 'X'): 
        text += result[length - 1]
    return text

text = "HELLO"
key = "CARNIVAL"

# text = input("\nEnter plain-text: ")
# key = input("Enter key: ")

encrypted = encrypt(text, key)
print("\nEncrypted: " + encrypted)
decrypted = decrypt(encrypted, key)
print("\nDecrypted: " + decrypted + "\n")