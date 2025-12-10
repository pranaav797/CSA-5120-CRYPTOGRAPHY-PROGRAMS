def otp_encrypt(pt, key):
    pt = pt.replace(" ", "").lower()
    cipher = ""
    for i, ch in enumerate(pt):
        shift = key[i]
        c = (ord(ch) - 97 + shift) % 26
        cipher += chr(c + 97)
    return cipher

plaintext = "send more money"
key = [9,0,1,7,23,15,21,14,11,11,2,8,9]
cipher = otp_encrypt(plaintext, key)
print("Ciphertext:", cipher)

def compute_key(cipher, target):
    cipher = cipher.replace(" ", "")
    target = target.replace(" ", "")
    key = []
    for c, t in zip(cipher, target):
        k = (ord(t)-97 - (ord(c)-97)) % 26
        key.append(k)
    return key

cipher = "output_from_part_a"
target = "cash not needed"

print("Required key:", compute_key(cipher, target))
