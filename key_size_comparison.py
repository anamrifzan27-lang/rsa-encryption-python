from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

recipe = b"Secret Recipe: Hot Chocolate Mix"

start_small = time.time()
small_key = RSA.generate(1024)
public_small = small_key.publickey()

cipher_small = PKCS1_OAEP.new(public_small)
ciphertext_small = cipher_small.encrypt(recipe)

dec_small = PKCS1_OAEP.new(small_key).decrypt(ciphertext_small)
end_small = time.time()


start_large = time.time()
large_key = RSA.generate(2048)
public_large = large_key.publickey()

cipher_large = PKCS1_OAEP.new(public_large)
ciphertext_large = cipher_large.encrypt(recipe)

dec_large = PKCS1_OAEP.new(large_key).decrypt(ciphertext_large)
end_large = time.time()


print("Decrypted with 1024-bit key:", dec_small)
print("1024-bit key time: {:.4f} seconds".format(end_small - start_small))

print("\nDecrypted with 2048-bit key:", dec_large)
print("2048-bit key time: {:.4f} seconds".format(end_large - start_large))

print("\nObservation: 1024-bit keys are faster but less secure; 2048-bit keys are stronger but slightly slower.")
