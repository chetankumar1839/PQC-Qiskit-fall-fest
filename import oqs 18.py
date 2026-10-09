import oqs

with oqs.Signature("ML-DSA-65") as signer:
    public_key = signer.generate_keypair()
    secret_key = signer.export_secret_key()

# Save the keys to files
with open("ml_dsa_public.key", "wb") as f:
    f.write(public_key)

with open("ml_dsa_secret.key", "wb") as f:
    f.write(secret_key)

print("Keys generated and saved successfully!")
print("Public key:", len(public_key), "bytes")
print("Secret key:", len(secret_key), "bytes")