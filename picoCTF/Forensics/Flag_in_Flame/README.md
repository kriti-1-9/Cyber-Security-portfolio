# Challenge: Flag in Flame (Log Forensics)

## Problem Statement
The SOC team discovered a suspiciously large log file after a recent breach. The file contained an enormous block of encoded text instead of typical log entries. The mission was to uncover the hidden data within this unusual log.

## Solution Path
This challenge required a multi-stage "Data Carving" approach to peel back several layers of obfuscation:

1. **Layer 1: Base64 Decoding**
   - Identified the large block of text as Base64.
   - Decoded the block, which revealed a PNG image file signature (`89 50 4E 47`).

2. **Layer 2: Binary Analysis**
   - Used `binwalk` to inspect the internal structure of the reconstructed PNG.
   - Discovered a Zlib compressed data stream embedded at offset `0x29`.

3. **Layer 3: Resilient Decompression**
   - Standard tools like `zlib-flate` failed due to a truncated/incomplete stream error.
   - Developed a Python script using `zlib.decompressobj()` to perform a streaming decompression, successfully bypassing the truncation error to reveal the hidden flag.

## SDE Takeaway
In a production environment, data is often corrupted or incomplete. This challenge demonstrated the necessity of moving beyond standard CLI tools and using low-level libraries (like Python's `zlib`) to build resilient recovery scripts.