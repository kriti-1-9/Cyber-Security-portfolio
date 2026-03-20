import base64
import zlib
import re

def solve_challenge():
    input_file = 'logs.txt'
    print(f"[*] Processing {input_file}...")

    try:
        # 1. Decode the Base64 block from the logs
        with open(input_file, 'r') as f:
            encoded_data = f.read().strip().replace('\n', '').replace('\r', '')
            raw_bytes = base64.b64decode(encoded_data)
        
        # 2. Extract Zlib data (we know from your binwalk it starts at offset 41)
        # We use decompressobj to handle the 'incomplete stream' error gracefully
        print("[*] Carving and decompressing Zlib stream...")
        zlib_data = raw_bytes[41:]
        dobj = zlib.decompressobj()
        
        try:
            decompressed_data = dobj.decompress(zlib_data)
        except zlib.error:
            # Grab whatever was successfully inflated before the error
            decompressed_data = dobj.unconsumed_tail 
            
        final_output = decompressed_data.decode('utf-8', errors='ignore')

        # 3. Find and print the flag
        flag = re.search(r'picoCTF\{.*?\}', final_output)
        if flag:
            print(f"\n[!] FLAG FOUND: {flag.group()}")
        else:
            # Fallback: Print strings if regex fails
            print("\n[!] Potential data recovered (check for flag):")
            print(final_output[:500])

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    solve_challenge()