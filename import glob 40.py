import glob
import shutil
import zipfile
import os

zip_files = glob.glob("/content/*.zip")

if not zip_files:
    raise FileNotFoundError("No ZIP file found in /content.")

original = zip_files[0]
tampered = "/content/tampered_copy.zip"

# Make a copy
shutil.copy2(original, tampered)

# Modify the copy
with zipfile.ZipFile(tampered, "a") as z:
    z.writestr(
        "tampered.txt",
        "This file was added after signing."
    )

print("✅ Tampered copy created!")
print("Original:", original)
print("Tampered:", tampered)