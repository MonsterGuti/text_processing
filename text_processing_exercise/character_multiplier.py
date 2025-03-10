f_word, s_word = input().split()
final_sum = 0

if len(f_word) > len(s_word):
    for index in range(len(s_word)):
        final_sum += ord(f_word[index]) * ord(s_word[index])
    for index in range(len(s_word), len(f_word)):
        final_sum += ord(f_word[index])

elif len(f_word) < len(s_word):
    for index in range(len(f_word)):
        final_sum += ord(f_word[index]) * ord(s_word[index])
    for index in range(len(f_word), len(s_word)):
        final_sum += ord(s_word[index])

else:
    for index in range(len(f_word)):
        final_sum += ord(f_word[index]) * ord(s_word[index])

print(final_sum)
