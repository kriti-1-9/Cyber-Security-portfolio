# Challenge: Hidden in Plain Sight (Steganography)

### 1. Investigation
The challenge provided a standard JPG image. I began by inspecting the file's metadata using `exiftool`. 

### 2. The Breakthrough
In the `Comment` metadata field, I discovered an obfuscated string: `steghide:cEF6endvcmQ=`. 
* The prefix indicated that the tool **Steghide** was required.
* The suffix `cEF6endvcmQ=` was a Base64-encoded passphrase.

### 3. Execution
1. **Decoding:** Decoded the Base64 string to retrieve the plain-text passphrase.
2. **Extraction:** Used the command `steghide extract -sf img.jpg` and provided the decoded passphrase.
3. **Recovery:** The extraction process yielded a file named `flag.txt`, which contained the final flag.

### 4. Key Takeaways
* **Metadata Risks:** Sensitive information (like passwords) is often accidentally left in file metadata.
* **Security through Obscurity:** Steganography is not a replacement for encryption, as tools like `steghide` and `exiftool` make extraction trivial once the method is identified.