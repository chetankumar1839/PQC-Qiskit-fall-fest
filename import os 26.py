import os

files = [
    "ml_dsa_public.key",
    "ml_dsa_secret.key",
    "message.txt",
    "message.sig"
]

for filename in files:
    print(f"{filename}: {os.path.getsize(filename)} bytes")