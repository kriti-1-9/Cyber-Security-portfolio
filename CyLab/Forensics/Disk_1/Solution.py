import re

def extract_flag_from_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()

    # Extract printable ASCII strings
    strings = re.findall(rb"[ -~]{4,}", data)

    for s in strings:
        if b"picoCTF{" in s:
            return s.decode()

    return "Flag not found."

if __name__ == "__main__":
    image_file = "disko-1.dd"
    flag = extract_flag_from_image(image_file)
    print(flag)