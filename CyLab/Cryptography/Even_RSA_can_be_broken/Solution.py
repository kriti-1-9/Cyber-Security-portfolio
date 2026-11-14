from Crypto.Util.number import inverse, long_to_bytes

N = YOUR_N
e = 65537
c = YOUR_CIPHERTEXT

p = 2
q = N // 2

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

m = pow(c, d, N)

print(long_to_bytes(m))