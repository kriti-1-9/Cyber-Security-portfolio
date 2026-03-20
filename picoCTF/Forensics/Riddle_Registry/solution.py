import base64
import subprocesses

# This script automates and decrypt the flag for the Riddle Registry challenge in picoCTF.
# The flag is encoded in base64, so we need to decode it first.
def solve_challenge():
    # The encoded string we found in the Author metadata
    encoded_string = "cGljb0NURntwdXp6bDNkX20zZGFkYXRhc19yYwdW5klv9IZTQ1NDk1MH0="
    
    try:
        # Decoding the Base64 string
        decoded_bytes = base64.b64decode(encoded_string)
        flag = decoded_bytes.decode('utf-8')
        
        print("-" * 20)
        print(f"SUCCESS: Flag found!")
        print(f"FLAG: {flag}")
        print("-" * 20)
        
    except Exception as e:
        print(f"Error decoding flag: {e}")

if __name__ == "__main__":
    solve_challenge()