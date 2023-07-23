
def decrypt_coordinates(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += decrypted_char
    return plaintext

ciphertext = "|OP�`Z<E]�|Y\\��$"
key = "Jai Shree Ram!"

decrypted_coordinates = decrypt_coordinates(ciphertext, key)
print(decrypted_coordinates)

# Save decrypted coordinates to a text file
with open("coordinates.txt", "w") as file:
    file.write(decrypted_coordinates)
