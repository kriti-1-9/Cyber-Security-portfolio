#!/usr/bin/env python3
"""
picoCTF - StegoRSA
Category: Cryptography
Author: Kriti

Solution script to automate:
  1. Extracting the hex-encoded private key from image EXIF metadata
  2. Decoding hex to PEM private key
  3. Decrypting the flag using RSA private key

Usage:
    python3 solution.py image.jpg flag.enc
"""

import subprocess
import sys
import os


def extract_hex_from_image(image_path):
    """Extract hex-encoded private key from image EXIF comment."""
    print(f"[*] Running exiftool on: {image_path}")
    result = subprocess.run(
        ["exiftool", image_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("[-] exiftool failed. Is it installed? sudo apt install libimage-exiftool-perl")
        sys.exit(1)

    # Look for Comment field in exiftool output
    for line in result.stdout.splitlines():
        if "Comment" in line:
            hex_data = line.split(":", 1)[1].strip()
            print(f"[+] Found comment field ({len(hex_data)} chars)")
            return hex_data

    print("[-] No Comment field found in image metadata.")
    sys.exit(1)


def hex_to_pem(hex_string, output_path="private_key.pem"):
    """Decode hex string to PEM private key file."""
    print(f"[*] Decoding hex to PEM key...")

    try:
        key_bytes = bytes.fromhex(hex_string)
        with open(output_path, "wb") as f:
            f.write(key_bytes)
        print(f"[+] Private key saved to: {output_path}")

        # Verify it looks like a PEM key
        key_text = key_bytes.decode("utf-8", errors="ignore")
        if "BEGIN" in key_text and "KEY" in key_text:
            print("[+] Valid PEM key confirmed!")
        else:
            print("[-] Warning: decoded data doesn't look like a PEM key")

        return output_path

    except ValueError as e:
        print(f"[-] Hex decoding failed: {e}")
        sys.exit(1)


def decrypt_flag(key_path, encrypted_flag_path, output_path="flag.txt"):
    """Decrypt the flag using RSA private key via openssl."""
    print(f"[*] Decrypting {encrypted_flag_path} with private key...")

    result = subprocess.run(
        ["openssl", "pkeyutl", "-decrypt",
         "-inkey", key_path,
         "-in", encrypted_flag_path,
         "-out", output_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"[-] openssl pkeyutl failed: {result.stderr}")
        # Try legacy rsautl as fallback
        print("[*] Trying legacy openssl rsautl...")
        result = subprocess.run(
            ["openssl", "rsautl", "-decrypt",
             "-inkey", key_path,
             "-in", encrypted_flag_path,
             "-out", output_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"[-] Both methods failed: {result.stderr}")
            sys.exit(1)

    with open(output_path, "r") as f:
        flag = f.read().strip()

    return flag


def main():
    # --- argument handling ---
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <image_file> <encrypted_flag_file>")
        print(f"Example: python3 {sys.argv[0]} image.jpg flag.enc")
        sys.exit(1)

    image_path = sys.argv[1]
    flag_enc_path = sys.argv[2]

    for path in [image_path, flag_enc_path]:
        if not os.path.exists(path):
            print(f"[-] File not found: {path}")
            sys.exit(1)

    print("=" * 50)
    print("  picoCTF - RSA Key in Image - Solver")
    print("=" * 50)

    # Step 1: Extract hex from image metadata
    hex_data = extract_hex_from_image(image_path)

    # Step 2: Decode hex to PEM key
    key_path = hex_to_pem(hex_data)

    # Step 3: Decrypt the flag
    flag = decrypt_flag(key_path, flag_enc_path)

    print("\n" + "=" * 50)
    print(f"[+] FLAG: {flag}")
    print("=" * 50)

    # Cleanup temp key file
    os.remove(key_path)
    print("[*] Cleaned up private_key.pem")


if __name__ == "__main__":
    main()