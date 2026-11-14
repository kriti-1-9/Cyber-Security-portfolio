# 🔐 Hash Crack
**Category:** Cryptography

## Challenge Overview
A company server was breached due to weakly hashed passwords.
The objective was to identify the hashing algorithm used and recover the original plaintext password.

## Initial Access
The challenge provided a remote service accessible via:
```
nc <server> <port>
```
Upon connection, the server displayed a hash and requested the corresponding password.

### Step 1 – Identify Hash Type
Given hash example:
```
482c811da5d5b4bc6d497ffa98491e38
```
Observations:
- 32 hexadecimal characters
- Likely MD5 (128-bit)
Using hash identification tools confirmed it as MD5.

### Step 2 – Crack the Hash
Since MD5 is a fast and weak hashing algorithm, dictionary attacks are effective.
Methods used:
- RockYou wordlist
- Online hash database verification
- Custom Python brute-force script
The password was successfully recovered.

### Step 3 – Authenticate
The cracked password was submitted back into the netcat session.
The server returned the flag.

## Key Takeaways
- MD5 is cryptographically broken for password storage.
- Fast hash functions allow efficient brute-force attacks.
- Password hashing should use:
    - bcrypt
    - Argon2
    - scrypt

## Security Insight
Weak hashing mechanisms combined with common passwords lead to full system compromise.
This challenge reinforces the importance of secure password storage practices.