import sys
import subprocess

result = subprocess.run(
    [sys.executable, "-m", "pip", "show", "liboqs-python"],
    capture_output=True,
    text=True
)

print(result.stdout)