def is_valid(name):
    if is_len_true(name) and is_written_by_letters(name) and no_redundant_symbols(name):
        return True
    return False


def is_len_true(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def is_written_by_letters(name):
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


user_input = input().split(", ")
for name in user_input:
    if is_valid(name):
        print(name)
