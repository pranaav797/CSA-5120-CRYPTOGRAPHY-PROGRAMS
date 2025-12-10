import numpy as np
import math

def mod_inverse(a, m):
    """Return modular inverse of a mod m, or None if not invertible."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def mod_inv_matrix(M, mod=26):
    det = int(round(np.linalg.det(M))) % mod
    det_inv = mod_inverse(det, mod)

    if det_inv is None:
        raise ValueError(f"Matrix not invertible mod {mod}. Determinant = {det}")

    adj = np.array([[M[1][1], -M[0][1]],
                    [-M[1][0], M[0][0]]])

    return (det_inv * adj) % mod

def recover_hill_key(plaintext_blocks, ciphertext_blocks):
    P = np.array(plaintext_blocks).T % 26
    C = np.array(ciphertext_blocks).T % 26
    
    # Check invertibility
    det = int(round(np.linalg.det(P))) % 26
    if math.gcd(det, 26) != 1:
        print("❌ ERROR: Plaintext matrix is NOT invertible modulo 26.")
        print(f"Determinant = {det}, gcd(det, 26) = {math.gcd(det, 26)}")
        return None

    P_inv = mod_inv_matrix(P, 26)
    K = (C.dot(P_inv)) % 26
    return K

# -------------------------
# TEST WITH USER DATA
# -------------------------

# Example pairs (YOU MUST REPLACE WITH VALID PAIRS)
plaintext = [[12, 4],   # m=12, e=4
             [4, 19]]   # e=4, t=19

cipher = [[2, 5],
          [7, 11]]

K = recover_hill_key(plaintext, cipher)

if K is not None:
    print("\nRecovered Hill key matrix:")
    print(K)
