import oqs

message = b"Hello, this is a real ML-DSA-65 test!"

with oqs.Signature("ML-DSA-65") as signer:
    public_key = signer.generate_keypair()
    secret_key = signer.export_secret_key()
    signature = signer.sign(message)

print("Public key size:", len(public_key), "bytes")
print("Secret key size:", len(secret_key), "bytes")
print("Signature size:", len(signature), "bytes")

with oqs.Signature("ML-DSA-65") as verifier:
    valid = verifier.verify(message, signature, public_key)

print("Signature valid:", valid)