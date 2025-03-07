user_input = input().split()
result = ""

for word in user_input:
    result += word * len(word)

print(result)