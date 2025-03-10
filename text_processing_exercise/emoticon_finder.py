user_sentence = input()

for index in range(len(user_sentence)):
    if user_sentence[index] == ":":
        print(f":{user_sentence[index + 1]}")