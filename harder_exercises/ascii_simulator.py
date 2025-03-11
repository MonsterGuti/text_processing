f_symbol = input()
s_symbol = input()
user_line = input()

ascii_sum = 0

for char in user_line:
    if ord(char) in range(ord(f_symbol) + 1, ord(s_symbol)):
        ascii_sum += ord(char)

print(ascii_sum)
