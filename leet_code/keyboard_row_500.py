from typing import List


def _valid(word: str) -> bool:
    first_row = "qwertyuiop"
    second_row = "asdfghjkl"
    third_row = "zxcvbnm"
    first_count = 0
    second_count = 0
    third_count = 0
    index = 0
    while index < len(word):
        if word[index].lower() in first_row:
            first_count += 1
        elif word[index].lower() in second_row:
            second_count += 1
        elif word[index].lower() in third_row:
            third_count += 1
        index += 1

    number_letters = len(word)
    return number_letters == first_count or number_letters == second_count or number_letters == third_count


def find_words(words: List[str]) -> List[str]:
    response = []
    for word in words:
        if _valid(word):
            response.append(word)
    return response
