import oqs

# Read the tampered ZIP
with open("/content/tampered_copy.zip", "rb") as f:
    tampered_data = f.read()

# Read the public key and original signature
with open("interface_public.key", "rb") as f:
    public_key = f.read()

with open("interface_signature.sig", "rb") as f:
    signature = f.read()

# Verify the tampered file
with oqs.Signature("ML-DSA-65") as verifier:
    valid = verifier.verify(
        tampered_data,
        signature,
        public_key
    )

print("Tampered ZIP signature valid:", valid)

if not valid:
    print("❌ TAMPERING DETECTED")
else:
    print("⚠️ Unexpected: signature still valid")