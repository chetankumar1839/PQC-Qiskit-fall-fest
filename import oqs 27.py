import oqs

with open("message.txt", "rb") as f:
    message = f.read()

with open("ml_dsa_public.key", "rb") as f:
    public_key = f.read()

with open("message.sig", "rb") as f:
    signature = f.read()

with oqs.Signature("ML-DSA-65") as verifier:
    valid = verifier.verify(message, signature, public_key)

if valid:
    print("✅ VERIFIED")
    print("The file has a valid ML-DSA-65 signature.")
else:
    print("❌ VERIFICATION FAILED")
    print("The signature does not match the file.")