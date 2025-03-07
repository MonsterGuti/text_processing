user_input = input()
digits = letters = others = ""

for char in user_input:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(f"{digits}\n{letters}\n{others}")
