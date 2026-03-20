def decode(enc):
    flag = ""

    for ch in enc:
        value = ord(ch)

        first = value >> 8
        second = value & 0xff

        flag += chr(first)
        flag += chr(second)

    return flag

enc = input("Enter encoded string: ")
print(decode(enc))