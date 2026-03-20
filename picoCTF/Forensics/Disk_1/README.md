# Category: Forensics

## Overview
In this challenge, we were given a compressed disk image file:
```
disko-1.dd.gz
```
The objective was to analyze the disk image and recover the hidden flag.
This challenge tested raw disk image handling, filesystem identification, and deleted file recovery concepts.

### Step 1 – Decompress the Disk Image
```
gunzip disko-1.dd.gz
```
This produced:
```
disko-1.dd
```

### Step 2 – Identify the Filesystem
We analyzed the file type:
```
file disko-1.dd
```
The output indicated:
```
FAT (32 bit)
```
This confirmed the disk image contained a FAT32 filesystem.

### Step 3 – Partition Analysis
Attempting to list partitions:
```
mmls disko-1.dd
```
No output was produced, indicating that:
- There was no partition table
- The filesystem started directly at offset 0

### Step 4 – Mount the Disk Image
The image was mounted for inspection:
```
mkdir mount
sudo mount -o loop disko-1.dd mount
ls mount
```
A /bin directory was present, containing many system binaries.
Manual browsing was inefficient due to the large number of files.

### Step 5 – Search Raw Disk Data
Instead of manually exploring mounted directories, we searched the entire raw disk image:
```
strings disko-1.dd | grep pico
```
This successfully revealed the flag.

## Why This Worked
- FAT32 does not securely wipe deleted files
- Deleted file contents often remain in raw disk sectors
- Mounted filesystems only show active files
- strings extracts printable ASCII directly from binary data
- By searching the raw image instead of the mounted filesystem, we were able to recover hidden or deleted data.

## Key Concepts Learned
- Disk images can be analyzed directly without mounting
- strings is powerful in forensic analysis
- Deleted files may still exist in raw disk sectors
- Understanding filesystem behavior is critical in CTF forensics challenges