plaintext = input("Input text term: ")
distance = int(input("Insert distance: "))

encrypted = ""

for char in plaintext:
    code = ord(char)

    if 32 <= code <= 126:
        shifted = 32 + ((code - 32 + distance) % 95)
        encrypted += chr(shifted)
    else:
        encrypted += char

print(encrypted)
