matrix = [
    ['M','F','H','I','K'],
    ['U','N','O','P','Q'],
    ['Z','V','W','X','Y'],
    ['E','L','A','R','G'],
    ['D','S','T','B','C']
]

def pos(c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j

def playfair_encrypt(text):
    text = text.upper().replace("J","I")
    text = "".join([c for c in text if c.isalpha()])

    # make digraphs
    i = 0
    pairs = []
    while i < len(text):
        a = text[i]
        if i+1 < len(text) and text[i+1] != a:
            b = text[i+1]
            i += 2
        else:
            b = 'X'
            i += 1
        pairs.append((a,b))

    cipher = ""
    for a,b in pairs:
        r1,c1 = pos(a)
        r2,c2 = pos(b)
        if r1==r2:
            cipher += matrix[r1][(c1+1)%5]
            cipher += matrix[r2][(c2+1)%5]
        elif c1==c2:
            cipher += matrix[(r1+1)%5][c1]
            cipher += matrix[(r2+1)%5][c2]
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]
    return cipher

msg = "Must see you over Cadogan West. Coming at once."
print("Plain Text:",msg)
print("Cipher Text:",playfair_encrypt(msg))
