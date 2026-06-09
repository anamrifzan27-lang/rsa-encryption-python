from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


# 1. Generate RSA Keys

key = RSA.generate(2048)

# Extract RSA mathematical values
p = key.p
q = key.q
n = key.n
phi_n = (p - 1) * (q - 1)
e = key.e
d = key.d

print("\n=== RSA Key Components ===")
print("p       =", p)
print("q       =", q)
print("n = p*q =", n)
print("phi(n)  =", phi_n)
print("e (public exponent)  =", e)
print("d (private exponent) =", d)


# 2. Prepare keys for encryption

public_key = key.publickey()
cipher_rsa = PKCS1_OAEP.new(public_key)


# 3. Encrypt a plaintext message

plaintext = b"Hot chocolate :Add 200g bittersweet chocolate to 300g boiling cream add vanilla shots and coco mix top with whip cream"



ciphertext = cipher_rsa.encrypt(plaintext)

print("\n=== RSA Encryption ===")
print("Plaintext:", plaintext)
print("Ciphertext (hex):", ciphertext.hex()[:100] + "...")


# 4. Decrypt the ciphertext

cipher_rsa_dec = PKCS1_OAEP.new(key)
decrypted = cipher_rsa_dec.decrypt(ciphertext)

print("\n=== RSA Decryption ===")
print("Decrypted:", decrypted)
print("Successful:", decrypted == plaintext)
