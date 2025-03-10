user_input = input().strip().split()
total_sum = 0

for word in user_input:
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    else:
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    else:
        number += (ord(last_letter) - 96)

    total_sum += number

print(f"{total_sum:.2f}")
