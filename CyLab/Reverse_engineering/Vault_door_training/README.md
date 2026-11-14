# Vault Door Training – Reverse Engineering Writeup

## Challenge

**Category:** Reverse Engineering
**Platform:** picoCTF

The mission is to retrieve the password required to unlock a vault door protecting Dr. Evil's laboratory.

Instead of guessing the password, the challenge provides the **source code** of the vault program. The task is to analyze the code and determine the correct password.

---

## Source Code Analysis

The provided program is written in Java and contains a function responsible for validating the password:

```
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt");
}
```

The program directly compares the user input with a **hardcoded string** using the `equals()` method.

Since the password is stored directly in the source code, we can extract it without executing or reversing the binary.

---

## Extracted Password

```
w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt
```

---

## Flag

The flag format for picoCTF challenges is:

```
picoCTF{password}
```

Final flag:

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}
```

---

## Key Learning

This challenge introduces **static analysis**, where the source code is examined directly to understand the program logic.

Hardcoding sensitive information such as passwords in source code is a serious security flaw because anyone with access to the code can retrieve it easily.

In real-world applications, secrets should be stored securely and never embedded directly in the source code.