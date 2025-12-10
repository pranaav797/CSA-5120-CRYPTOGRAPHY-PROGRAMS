def keyword_cipher_encrypt(plain, keyword="CIPHER"):
    keyword = "".join(dict.fromkeys(keyword.lower()))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    remaining = "".join([c for c in alphabet if c not in keyword])
    cipher = keyword + remaining

    table = {alphabet[i]: cipher[i] for i in range(26)}
    result = ""
    for ch in plain.lower():
        if ch.isalpha():
            result += table[ch]
        else:
            result += ch
    return result

print("Cipher Text:", keyword_cipher_encrypt("attack at dawn"))
