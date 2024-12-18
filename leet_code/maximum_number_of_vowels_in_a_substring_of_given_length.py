def _count_vowels(sentence: str) -> int:
    vowels = "aeiou"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count


def max_vowels(s: str, k: int) -> int:
    vowels = "aeiou"
    index = 0
    maximum_number_of_vowels = 0
    number_vowels = _count_vowels(s[index:index + k])
    while index + k <= len(s):
        if number_vowels > maximum_number_of_vowels:
            maximum_number_of_vowels = number_vowels
        if s[index] in vowels:
            number_vowels -= 1
        if index + k < len(s) and s[index + k] in vowels:
            number_vowels += 1
        index += 1
    return maximum_number_of_vowels
