while True:
    user_input = input()
    if user_input == "end":
        break
    new_string = user_input[::-1]
    print(f"{user_input} = {new_string}")
