user_word = input()
user_input = input()

while user_word in user_input:
    user_input = user_input.replace(user_word, "")

print(user_input)