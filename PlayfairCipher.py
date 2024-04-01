def prepare_input(text):
    # Convert the text to uppercase and replace J with I
    text = text.upper().replace("J", "I")
    # Remove any characters that are not letters
    text = ''.join(filter(str.isalpha, text))
    return text

def generate_key_square(key):
    key_square = [['' for _ in range(5)] for _ in range(5)]
    key_set = set()

    # Create the key square
    i, j = 0, 0
    for letter in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if letter not in key_set:
            key_square[i][j] = letter
            key_set.add(letter)
            j += 1
            if j == 5:
                j = 0
                i += 1

    return key_square

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def encrypt_pair(pair, key_square):
    (x1, y1), (x2, y2) = find_position(key_square, pair[0]), find_position(key_square, pair[1])

    if x1 == x2:
        return key_square[x1][(y1 + 1) % 5] + key_square[x2][(y2 + 1) % 5]
    elif y1 == y2:
        return key_square[(x1 + 1) % 5][y1] + key_square[(x2 + 1) % 5][y2]
    else:
        return key_square[x1][y2] + key_square[x2][y1]

def playfair_encrypt(plaintext, key):
    plaintext = prepare_input(plaintext)
    key_square = generate_key_square(key)

    encrypted_text = ''
    i = 0
    while i < len(plaintext):
        pair = plaintext[i:i + 2]
        if len(pair) == 1:
            pair += 'X'
            i -= 1

        encrypted_text += encrypt_pair(pair, key_square)
        i += 2

    return encrypted_text

# Example usage:
plaintext = "NATNAEL"
key = "SECRETKEY"

cipher_text = playfair_encrypt(plaintext, key)
print("Original Text:", plaintext)
print("Encrypted Text:", cipher_text)
