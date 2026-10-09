import glob
import os

zip_files = []

for folder in ["/tmp/gradio", "/content", "/mnt/data"]:
    zip_files.extend(
        glob.glob(folder + "/**/*.zip", recursive=True)
    )

print("ZIP files found:")
for i, path in enumerate(zip_files):
    print(i, "→", path)

if not zip_files:
    print("\n❌ No ZIP file found.")
else:
    print("\n✅ Found", len(zip_files), "ZIP file(s).")