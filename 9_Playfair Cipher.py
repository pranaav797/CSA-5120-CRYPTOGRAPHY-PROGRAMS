import re

def playfair_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    seq = []

    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            seq.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seq.append(ch)

    return [seq[i:i+5] for i in range(0, 25, 5)]


def pos(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


# Keep spaces & format
def clean_with_format(cipher):
    cleaned = []
    for ch in cipher:
        if ch.isalpha():
            cleaned.append(ch.upper().replace("J", "I"))
        else:
            cleaned.append(ch)
    return cleaned


def remove_filler_x(text):
    # Remove internal 'X' only when it is between identical letters from Playfair padding
    text = re.sub(r'([A-Z])X([A-Z])', r'\1\2', text)

    # Remove X at the end of words (padding)
    text = re.sub(r'X(\s|$)', r'\1', text)

    return text


def playfair_decrypt(cipher, key):
    arr = clean_with_format(cipher)
    M = playfair_matrix(key)
    pt = ""
    i = 0

    while i < len(arr):

        if not arr[i].isalpha():
            pt += arr[i]
            i += 1
            continue

        a = arr[i]

        j = i + 1
        while j < len(arr) and not arr[j].isalpha():
            pt += arr[j]
            j += 1

        if j >= len(arr):
            break

        b = arr[j]

        r1, c1 = pos(M, a)
        r2, c2 = pos(M, b)

        # Same row
        if r1 == r2:
            pt += M[r1][(c1 - 1) % 5]
            pt += M[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            pt += M[(r1 - 1) % 5][c1]
            pt += M[(r2 - 1) % 5][c2]

        # Rectangle rule
        else:
            pt += M[r1][c2]
            pt += M[r2][c1]

        i = j + 1

    # NEW: auto remove Playfair padding X
    pt = remove_filler_x(pt)

    return pt


cipher = """KX IEYU REB EZW EHEW RYTU HE YFSKR EH EGOYFIWU QUTQYO MUQ YCAIP OBOOEXUKN BOUKNO BOTF RBWB ONEYCU ZWRGNON SSZ TURZOKZVYOUZSKRE"""

print(playfair_decrypt(cipher, "royal new zealand navy"))
