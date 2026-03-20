# Even RSA Can Be Broken – Crypto Challenge Writeup
## Challenge
**Category:** Cryptography
**Platform:** picoCTF
The service provides an encrypted flag. We are given the RSA public key components and ciphertext:
* **N** (modulus)
* **e** (public exponent)
* **ciphertext**

Goal: Recover the original plaintext (flag).

---

## Provided Values

```
e = 65537
N = <large number>
ciphertext = <large number>
```

---

## Source Code Analysis

The encryption script performs standard RSA encryption:

```
c = m^e mod N
```

Where:

* `m` = plaintext message (flag)
* `e` = public exponent
* `N` = modulus
* `c` = ciphertext

During key generation:

```
p, q = get_primes(k//2)
N = p * q
```

RSA security depends on **both primes being large and unpredictable**.

---

## Vulnerability

In this challenge, one of the primes used in key generation is **2**, which is not secure.

Thus:

```
N = 2 × q
```

This means we can directly compute:

```
q = N / 2
```

Once the primes are known, the private key can be reconstructed.

---

## Attack Steps

1. Compute `q`:

```
q = N // 2
```

2. Compute Euler’s totient:

```
phi
```