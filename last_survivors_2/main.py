def get_next(letter):
    return 'a' if letter == 'z' else chr(ord(letter) + 1)


def find_double_letters(string):
    n = len(string)
    for i in range(0, n):
        j = string.find(string[i], i + 1)
        if j != -1:
            return i, j
    return None


def update_string(string):
    doubles = find_double_letters(string)
    if doubles is None:
        return False, string

    i, j = doubles
    letter = string[i]
    next_letter = get_next(letter)
    updated_string = string[:i] + next_letter + string[i + 1:j] + string[j + 1:]

    return True, updated_string


def last_survivors(string):
    while True:
        is_updated, string = update_string(string)
        if not is_updated:
            break
    return string
