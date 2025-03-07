banned_words = input().split(", ")
user_input = input()

for word in banned_words:
    while word in user_input:
        user_input = user_input.replace(word, "*" * len(word))

print(user_input)