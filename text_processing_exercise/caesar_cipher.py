user_input = input()
encrypted_message = ""

for char in user_input:
    encrypted_message += chr(ord(char) + 3)

print(encrypted_message)