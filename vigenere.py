def encrypt_vigenere(plaintext, keyword):
    ciphertext = ""
    index = 0
    keyindex = 0
    while index in range(len(plaintext)):
        if ord(plaintext[index].upper()) + ord(keyword[keyindex].upper()) - 65 > ord('Z'):
            ciphertext += chr(ord(plaintext[index]) + ord(keyword[keyindex].upper()) - 65 - 26)
        else:
            ciphertext += chr(ord(plaintext[index]) + ord(keyword[keyindex].upper()) - 65)
        if keyindex == len(keyword) - 1:
            keyindex = 0
        else:
            keyindex += 1
        index += 1
    print(ciphertext)
    return ciphertext
encrypt_vigenere("PYTHON", "A")
encrypt_vigenere("python", "a")
encrypt_vigenere("Python", "A")
encrypt_vigenere("ATTACKATDAWN", "LEMON")


def decrypt_vigenere(ciphertext, keyword):
    plaintext = ""
    index = 0
    keyindex = 0
    while index in range(len(ciphertext)):
        if ord(ciphertext[index].upper()) - ord(keyword[keyindex].upper()) + 65 < ord('A'):
            plaintext += chr(ord(ciphertext[index])- ord(keyword[keyindex].upper()) + 65 + 26)
        else:
            plaintext += chr(ord(ciphertext[index])- ord(keyword[keyindex].upper()) + 65)
        if keyindex == len(keyword) - 1:
            keyindex = 0
        else:
            keyindex += 1
        index += 1
    print(plaintext)
    return plaintext
decrypt_vigenere("PYTHON", "A")
decrypt_vigenere("python", "a")
decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
