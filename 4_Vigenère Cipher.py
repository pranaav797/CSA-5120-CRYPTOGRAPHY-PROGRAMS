def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()
    cipher = ""

    k = 0
    for ch in plaintext:
        if ch.isalpha():
            shift = ord(key[k % len(key)]) - ord('a')
            new = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            cipher += new
            k += 1
        else:
            cipher += ch
    return cipher


# ---- MAIN ----
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

encrypted = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted)
