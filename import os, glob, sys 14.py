import os, glob, sys

libs = glob.glob("/root/liboqs/build/lib/liboqs.so*")
print("Found:", libs)

if not libs:
    raise FileNotFoundError("liboqs.so was not found in the build directory.")

os.environ["OQS_INSTALL_PATH"] = "/root/liboqs/build"
sys.modules.pop("oqs", None)

import oqs

print("liboqs-python version:", oqs.oqs_python_version())
print("liboqs version:", oqs.oqs_version())
print("ML-DSA-65 available:", "ML-DSA-65" in oqs.get_enabled_sig_mechanisms())