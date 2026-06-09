# RSA Encryption & Decryption in Python

A Python implementation of RSA asymmetric encryption and decryption,
demonstrating how public and private keys protect sensitive data.

Built as part of my BSc Cybersecurity & Digital Forensics coursework
at Kingston University.

---

## What it does
- Generates 2048-bit RSA key pairs
- Displays RSA mathematical components (p, q, n, phi, e, d)
- Encrypts plaintext using the public key
- Decrypts ciphertext using the private key
- Verifies decrypted output matches original plaintext
- Compares performance and security of 1024-bit vs 2048-bit keys

---

## Files
- `rsa_encryption.py` — Main RSA encryption and decryption 
  implementation applied to a real-world scenario (Vintage Point Café 
  protecting confidential recipes)
- `key_size_comparison.py` — Demonstrates the security vs performance 
  tradeoff between 1024-bit and 2048-bit RSA keys

---

## Tools & Libraries
- Python 3
- pycryptodome — RSA key generation, encryption, decryption

Install dependency:
pip install pycryptodome

---

## How to run

Run the main RSA implementation:
python rsa_encryption.py

Run the key size comparison:
python key_size_comparison.py

---

## Key concepts demonstrated
- Asymmetric encryption (public/private key pairs)
- RSA mathematical foundations (prime numbers, modulus, Euler's totient)
- PKCS1_OAEP padding for secure encryption
- Key size impact on security and performance
- Real-world application: protecting confidential business data

---

*Academic project — BSc Cybersecurity & Digital Forensics,
Kingston University*
