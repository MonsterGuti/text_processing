text = input()
final_text = sub_string = repetitions = ""

for index in range(len(text)):
    if not text[index].isdigit():
        sub_string += text[index].upper()
    else:
        for next_symbol_index in range(index, len(text)):
            if not text[next_symbol_index].isdigit():
                break
            repetitions += text[next_symbol_index]

        final_text += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(final_text))}")
print(final_text)
