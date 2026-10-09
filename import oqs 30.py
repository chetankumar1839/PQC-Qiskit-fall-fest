import oqs

def verify_file(filename, signature_file):
    # Read the file
    with open(filename, "rb") as f:
        data = f.read()

    # Read public key
    with open("ml_dsa_public.key", "rb") as f:
        public_key = f.read()

    # Read signature
    with open(signature_file, "rb") as f:
        signature = f.read()

    # Verify
    with oqs.Signature("ML-DSA-65") as verifier:
        valid = verifier.verify(data, signature, public_key)

    if valid:
        print("✅ VERIFIED")
        print("File:", filename)
    else:
        print("❌ VERIFICATION FAILED")
        print("File:", filename)

    return valid


verify_file("message.txt", "message.txt.sig")