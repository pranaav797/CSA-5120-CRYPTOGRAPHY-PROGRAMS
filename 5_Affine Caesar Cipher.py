import string
alphabet = string.ascii_lowercase

def affine_encrypt(plain, a, b):
    cipher = ""
    for ch in plain.lower():
        if ch.isalpha():
            p = ord(ch) - 97
            c = (a*p + b) % 26
            cipher += chr(c + 97)
        else:
            cipher += ch
    return cipher

def affine_decrypt(cipher, a, b):
    # find modular inverse of a mod 26
    for x in range(26):
        if (a*x) % 26 == 1:
            a_inv = x
            break
    plain = ""
    for ch in cipher:
        if ch.isalpha():
            c = ord(ch) - 97
            p = (a_inv*(c - b)) % 26
            plain += chr(p + 97)
        else:
            plain += ch
    return plain

print("Encrypted:", affine_encrypt("hello", 5, 8))
print("Decrypted:", affine_decrypt(affine_encrypt("hello", 5, 8), 5, 8))
