import oqs

message = b"ML-DSA-65 protects this message."

# 1. Generate key pair
with oqs.Signature("ML-DSA-65") as signer:
    public_key = signer.generate_keypair()
    secret_key = signer.export_secret_key()
    signature = signer.sign(message)

# 2. Verify original message
with oqs.Signature("ML-DSA-65") as verifier:
    original_valid = verifier.verify(
        message, signature, public_key
    )

# 3. Tamper with the message
tampered_message = b"ML-DSA-65 message was modified!"

with oqs.Signature("ML-DSA-65") as verifier:
    tampered_valid = verifier.verify(
        tampered_message, signature, public_key
    )

# Results
print("=== ML-DSA-65 FINAL TEST ===")
print("Public key:", len(public_key), "bytes")
print("Secret key:", len(secret_key), "bytes")
print("Signature:", len(signature), "bytes")
print()
print("Original message:", original_valid)
print("Tampered message:", tampered_valid)

if original_valid and not tampered_valid:
    print("\n✅ ML-DSA-65 TEST PASSED")
else:
    print("\n❌ TEST FAILED")