user_input = input()

last_checked_element = filtered_string = ""
for char in user_input:
    if char != last_checked_element:
        last_checked_element = char
        filtered_string += char

print(filtered_string)