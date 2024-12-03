from collections import Counter


def first_unique_character(s: str) -> int:
    response = -1
    counter = Counter(s)
    index = 0
    while index < len(s):
        current = s[index]
        if counter[current] == 1:
            return index
        index += 1
    return response
