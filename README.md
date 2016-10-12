def encrypt_caesar(plaintext):
    ciphertext = ""
    for symbol in plaintext:
        if ord(symbol.upper()) + 3 > ord('Z'):
            ciphertext += chr(ord(symbol) + 3 - 26)
        else:
            ciphertext += chr(ord(symbol) + 3)
    print(ciphertext)
    return ciphertext
encrypt_caesar("PYTHON")
encrypt_caesar("python")

def decrypt_caesar(ciphertext):
    plaintext = ""
    for symbol in ciphertext:
        if ord(symbol.upper()) - 3 < ord('A'):
            plaintext += chr(ord(symbol) - 3 + 26)
        else:
            plaintext += chr(ord(symbol) - 3)
    print(plaintext)
    return plaintext
decrypt_caesar("SBWKRQ")
decrypt_caesar("sbwkrq")
