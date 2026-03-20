import re

# Read the provided Java source file
with open("VaultDoorTraining.java", "r") as file:
    data = file.read()

# Search for the password inside equals("...")
match = re.search(r'equals\("(.+?)"\)', data)

if match:
    password = match.group(1)
    print("Password:", password)
    print("Flag: picoCTF{" + password + "}")
else:
    print("Password not found.")