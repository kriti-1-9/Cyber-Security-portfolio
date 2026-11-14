# 🔄 Transformation
---
## 🧩 Challenge Description
We were given the following encoding logic:
```python
enc = "".join([chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
               for i in range(0, len(flag), 2)])
```
The task was to determine what this transformation does and recover the original flag.

## 🔍 Analysis
Let’s break down the transformation:
```python
(ord(flag[i]) << 8) + ord(flag[i + 1])
```
Step-by-step breakdown:
1. `ord(flag[i])`
Converts the character to its ASCII value.

2. `<< 8`
Left shifts the ASCII value by 8 bits (equivalent to multiplying by 256).

3. `+ ord(flag[i + 1])`
Adds the ASCII value of the next character.

#### What does this mean?
Two characters are combined into a single 16-bit value:
```
[ first_char (8 bits) ][ second_char (8 bits) ]
```
Then:
```python
chr(combined_value)
```
This converts the 16-bit integer into a Unicode character.

As a result:
- The encoded string length is half of the original flag length.
- Every 2 characters are packed into 1 character.

## 🔓 Reversing the Transformation
If encoding is:
```
combined = (a << 8) + b
```
Then decoding is:
```
a = combined >> 8
b = combined & 0xff
```
Where:
- `>> 8` extracts the first byte
- `& 0xff` extracts the second byte

## 🧠 Concepts Learned
- Bitwise operations (`<<`, `>>`, `&`)
- Byte packing and unpacking
- Manual encoding/decoding logic
- Understanding custom data transformations

## 🎯 Key Takeaway
This challenge demonstrates how simple bit manipulation can transform data into a custom encoding format. By carefully analyzing the logic and reversing the operations step-by-step, we can reconstruct the original input.

Reverse engineering is often about understanding how data is transformed — not just analyzing binaries.
---