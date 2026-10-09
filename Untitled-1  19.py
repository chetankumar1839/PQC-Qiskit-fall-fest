message = b"This file is protected using ML-DSA-65."

with open("message.txt", "wb") as f:
    f.write(message)

print("message.txt created successfully!")
print("Content:", message.decode())