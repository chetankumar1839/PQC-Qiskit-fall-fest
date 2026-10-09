import oqs

# Read the message
with open("message.txt", "rb") as f:
    message = f.read()

# Read the secret key
with open("ml_dsa_secret.key", "rb") as f:
    secret_key = f.read()

# Create signer and import the secret key
with oqs.Signature("ML-DSA-65", secret_key) as signer:
    signature = signer.sign(message)

# Save the signature
with open("message.sig", "wb") as f:
    f.write(signature)

print("File signed successfully!")
print("Signature size:", len(signature), "bytes")
print("Saved as: message.sig")