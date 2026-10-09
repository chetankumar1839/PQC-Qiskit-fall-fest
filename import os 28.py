import os
import shutil

os.makedirs("ML_DSA_Project", exist_ok=True)

files = [
    "ml_dsa_public.key",
    "ml_dsa_secret.key",
    "message.txt",
    "message.sig"
]

for filename in files:
    shutil.copy(filename, "ML_DSA_Project/")

print("✅ ML-DSA project packaged successfully!")
print("\nFiles:")
for filename in os.listdir("ML_DSA_Project"):
    print(" -", filename)