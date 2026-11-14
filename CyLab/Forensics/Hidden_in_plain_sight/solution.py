import subprocess
import base64
import os

def solve():
    # 1. The data I found in the JPG's 'Comment' field
    # Format was "steghide:cEF6endvcmQ="
    encoded_passphrase = "cEF6endvcmQ=" 
    
    # 2. Decode the Base64 passphrase
    # In my case, 'cEF6endvcmQ=' decodes to 'pAzsw0rd'
    decoded_pass = base64.b64decode(encoded_passphrase).decode()
    print(f"[*] Extracted Passphrase: {decoded_pass}")
    
    # 3. Run Steghide to extract the hidden payload
    # '-p' allows us to pass the password via the script
    # '-f' forces overwrite if the file already exists
    try:
        print("[*] Extracting hidden data from img.jpg...")
        subprocess.run(
            ["steghide", "extract", "-sf", "img.jpg", "-p", decoded_pass, "-f"],
            check=True,
            capture_output=True
        )
        
        # 4. Read the flag from the extracted file
        if os.path.exists('flag.txt'):
            with open('flag.txt', 'r') as f:
                flag = f.read().strip()
                print(f"\n[!] SUCCESS! Flag Found: {flag}")
        else:
            print("[-] Error: flag.txt was not created.")

    except subprocess.CalledProcessError as e:
        print(f"[-] Steghide failed: {e}")
    except FileNotFoundError:
        print("[-] Error: Steghide is not installed or img.jpg is missing.")

if __name__ == "__main__":
    solve()