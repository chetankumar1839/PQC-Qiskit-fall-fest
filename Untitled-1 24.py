original_message = b"This file is protected using ML-DSA-65."

with open("message.txt", "wb") as f:
    f.write(original_message)

print("Original message restored!")