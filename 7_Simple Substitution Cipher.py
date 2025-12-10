import re
from collections import Counter

cipher_text = """53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83
(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*
;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"""

# Count symbol frequencies
freq = Counter(cipher_text)

print("=== Symbol Frequency ===")
for ch, count in freq.most_common():
    if ch.strip() != "":
        print(f"{repr(ch)} : {count}")

# Manual substitution mapping (derived from cryptanalysis)
mapping = {
    '‡': 't', '†': 'h', '8': 'e', '4': 'a', '6': 'n', '5': 'i',
    '3': 's', '0': 'd', '2': 'o', ')': ' ', ';': 'r', '*': 'c',
    '(': 'b', '¶': 'l', ']': 'f', '?': 'm', '—': 'p', '9': 'y',
    '1': 'g'
}

def decrypt(cipher, mapping):
    result = ""
    for ch in cipher:
        if ch in mapping:
            result += mapping[ch]
        else:
            result += ch
    return result

plaintext = decrypt(cipher_text, mapping)

print("\n=== Decrypted Text ===")
print(plaintext)
