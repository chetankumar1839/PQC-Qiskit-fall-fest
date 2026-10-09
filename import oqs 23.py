import oqs

# Tamper with the file
tampered_message = b"This file has been changed!"

with open("message.txt", "wb") as f:
    f.write(tampered_message)

# Load public key and old signature
with open("ml_dsa_public.key", "rb") as f:
    public_key = f.read()

with open("message.sig", "rb") as f:
    signature = f.read()

# Verify the tampered file
with oqs.Signature("ML-DSA-65") as verifier:
    valid = verifier.verify(tampered_message, signature, public_key)

print("Tampered file signature valid:", valid)