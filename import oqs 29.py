import oqs

def sign_file(filename):
    # Read the file
    with open(filename, "rb") as f:
        data = f.read()

    # Load secret key
    with open("ml_dsa_secret.key", "rb") as f:
        secret_key = f.read()

    # Sign
    with oqs.Signature("ML-DSA-65", secret_key) as signer:
        signature = signer.sign(data)

    # Save signature
    signature_file = filename + ".sig"
    with open(signature_file, "wb") as f:
        f.write(signature)

    print("✅ File signed successfully!")
    print("File:", filename)
    print("Signature:", signature_file)
    print("Signature size:", len(signature), "bytes")


sign_file("message.txt")