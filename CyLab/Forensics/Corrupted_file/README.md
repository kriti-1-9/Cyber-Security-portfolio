# Category: Forensics / Steganography

## Overview
In this challenge, we were provided with a corrupted image file. The objective was to analyze the file, identify hidden data, and recover the flag.

This challenge tested metadata analysis, base64 decoding, and steganography extraction techniques.

### Step 1 – Inspect Metadata
We first analyzed the image metadata using:
```
exiftool image.jpg
```
While reviewing the output, a suspicious Base64-encoded string was discovered in the comment field:
```
C3RlZ2hpZGU6Y0VGNmVuZHZjbVE9
```

### Step 2 – Decode the Base64 String
The string was decoded using:
```
echo "C3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 -d
```
Decoded output:
```
steghide:<password>
```
This revealed that the image likely contained hidden data embedded using steghide, along with the password required for extraction.

### Step 3 – Extract Hidden Data
Using the decoded password, we extracted the embedded file:
```
steghide extract -sf image.jpg
```
After entering the password when prompted, the tool produced:
```
flag.txt
```

### Step 4 – Retrieve the Flag
```
cat flag.txt
```
The flag was successfully recovered.

## Key Concepts Learned
- Metadata can contain hidden clues
- Base64 encoding is commonly used to obfuscate hints
- Steganography tools like steghide can embed files inside images
- Always inspect metadata before brute-forcing