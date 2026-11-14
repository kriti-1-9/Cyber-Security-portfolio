import hashlib

def crack_md5(hash_value, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.md5(word.encode()).hexdigest()
                
                if hashed_word == hash_value:
                    return word
        return None
    except FileNotFoundError:
        print("Wordlist file not found.")
        return None


if __name__ == "__main__":
    hash_input = input("Enter MD5 hash: ").strip()
    wordlist = "/usr/share/wordlists/rockyou.txt"

    result = crack_md5(hash_input, wordlist)

    if result:
        print(f"[+] Password Found: {result}")
    else:
        print("[-] Password not found in wordlist.")