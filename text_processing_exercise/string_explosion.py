user_input = input()
result = ""
explosion_power = 0

for i in range(len(user_input)):
    if user_input[i] == ">":
        result += ">"
        explosion_power += int(user_input[i + 1])
    elif explosion_power > 0:
        explosion_power -= 1
    else:
        result += user_input[i]

print(result)
