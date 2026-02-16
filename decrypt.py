encrypted = input("Enter encrypted prompt: ")
distance = int(input("Enter distance prompt: "))

plaintext = ""

for char in encrypted:
    code = ord(char)

    if 32 <= code <= 126:
        shifted = 32 + ((code - 32 - distance) % 95)
        plaintext += chr(shifted)
    else:
        plaintext += char

print(plaintext)
