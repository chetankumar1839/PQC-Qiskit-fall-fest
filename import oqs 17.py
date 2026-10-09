import oqs

# Original message
message = b"Hello, this is a real ML-DSA-65 test!"

# Generate keys and sign the original message
with oqs.Signature("ML-DSA-65") as signer:
    public_key = signer.generate_keypair()
    secret_key = signer.export_secret_key()
    signature = signer.sign(message)

# Verify the original message
with oqs.Signature("ML-DSA-65") as verifier:
    original_valid = verifier.verify(message, signature, public_key)

# Change the message AFTER it was signed
tampered_message = b"Hello, this message has been changed!"

# Verify the modified message using the original signature
with oqs.Signature("ML-DSA-65") as verifier:
    tampered_valid = verifier.verify(
        tampered_message,
        signature,
        public_key
    )

print("Original message valid :", original_valid)
print("Tampered message valid :", tampered_valid)