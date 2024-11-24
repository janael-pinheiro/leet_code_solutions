import string


def detect_capital_use(word: str) -> bool:
    number_capital_letters = 0
    index = 0
    while index < len(word):
        if word[index] in string.ascii_uppercase:
            number_capital_letters += 1
        index += 1
    if number_capital_letters == len(word) or number_capital_letters == 0:
        return True
    elif word[0] in string.ascii_uppercase and all([x not in string.ascii_uppercase for x in word[1:]]):
        return True
    return False
