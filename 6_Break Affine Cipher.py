def affine_decrypt(cipher, a, b):
    for x in range(26):
        if (a*x) % 26 == 1:
            a_inv = x
            break
    plain = ""
    for ch in cipher.lower():
        if ch.isalpha():
            c = ord(ch)-97
            p = (a_inv*(c-b)) % 26
            plain += chr(p+97)
        else:
            plain += ch
    return plain

cipher = "puupvt pu fcvb"
print("Cipher Text:",cipher)
print("Plaintext =", affine_decrypt(cipher, 3, 15))
