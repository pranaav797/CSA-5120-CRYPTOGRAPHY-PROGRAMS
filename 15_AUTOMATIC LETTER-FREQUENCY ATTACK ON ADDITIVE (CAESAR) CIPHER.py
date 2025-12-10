from collections import Counter

def caesar_decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = 'a'
            result += chr((ord(ch)-ord(base)-shift)%26 + ord(base))
        else:
            result += ch
    return result

def attack_caesar(cipher, top_n=10):
    english_freq_order = "etaoinshrdlucmfwypvbgkjqxz"
    results = []
    for shift in range(26):
        pt = caesar_decrypt(cipher, shift)
        freq = Counter(pt.replace(" ", ""))
        score = sum(freq[ch] * (26-i) for i, ch in enumerate(english_freq_order))
        results.append((score, shift, pt))
    results.sort(reverse=True)

    for _, shift, text in results[:top_n]:
        print(f"[Shift {shift}] --> {text}")

cipher = input("Enter ciphertext: ")
attack_caesar(cipher, top_n=10)
