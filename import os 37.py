import os
import glob

zip_files = glob.glob("/tmp/gradio/**/*.zip", recursive=True)

print("ZIP files found:")
for f in zip_files:
    print(f)