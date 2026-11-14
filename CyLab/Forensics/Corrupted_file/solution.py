import subprocess
import base64
import re

IMAGE = "image.jpg"

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

print("[+] Reading metadata with exiftool...")
meta = run(f"exiftool {IMAGE}")

# Find base64 string inside metadata
match = re.search(r'[A-Za-z0-9+/=]{20,}', meta)

if not match:
    print("[-] No encoded string found.")
    exit()

encoded = match.group(0)
print(f"[+] Found encoded string: {encoded}")

decoded = base64.b64decode(encoded).decode()
print(f"[+] Decoded string: {decoded}")

# Extract password after colon
if ":" in decoded:
    password = decoded.split(":")[1]
else:
    password = decoded

print(f"[+] Using password: {password}")

print("[+] Running steghide extraction...")
subprocess.run(f"steghide extract -sf {IMAGE} -p {password}", shell=True)

print("[+] Done. Check flag.txt")