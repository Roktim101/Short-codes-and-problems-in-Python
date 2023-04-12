string = "5.6.7x2.9.10x2.12.15 "

# Remember to put sub-strings according to their priority in orders.
replacements = {" ": " and more", ".": ", ", "x": "*"}

for old_substring, new_substring in replacements.items():
    string = string.replace(old_substring, new_substring)

print(string)

# CTRL + r: Replace function in PyCharm
# CTRL + f: Find function in PyCharm
