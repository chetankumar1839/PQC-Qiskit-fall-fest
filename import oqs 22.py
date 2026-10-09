import oqs

# Read the original message
with open("message.txt", "rb") as f:
    message = f.read()

# Read the public key
with open("ml_dsa_public.key", "rb") as f:
    public_key = f.read()

# Read the signature
with open("message.sig", "rb") as f:
    signature = f.read()

# Verify the signature
with oqs.Signature("ML-DSA-65") as verifier:
    valid = verifier.verify(message, signature, public_key)

print("Signature valid:", valid)