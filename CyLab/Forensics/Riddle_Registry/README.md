# Challenge: Riddle Registry (picoCTF)

### 1. The Problem
The challenge provided a PDF file (`confidential.pdf`) that appeared to contain placeholder text. Standard text searches (`grep`) for the flag pattern failed because the sensitive data was not stored in the document body, but was hidden within the file's **XMP Metadata**. Specifically, the `Author` field contained a string that looked like gibberish but featured a trailing `=` sign—a signature of Base64 encoding.

### 2. The Solution
I used the Kali Linux utility `exiftool` to inspect the document's metadata. After identifying the suspicious string in the Author field, I utilized the `base64` decoding utility in the terminal to revert the obfuscated text into its original format. I then developed a Python script (`solution.py`) to automate this decoding process, ensuring the solution is repeatable.

### 3. The Lesson (SDE Perspective)
This challenge highlights a common data leakage vulnerability: **Metadata Over-retention**. Developers often forget that file properties (EXIF, XMP) are as accessible as the file content itself. From a Secure Development Lifecycle (SDL) standpoint, any public-facing assets should undergo a "sanitization" pass using tools like `exiftool` to strip internal metadata before deployment. Encoding is not encryption; never rely on Base64 to protect secrets.