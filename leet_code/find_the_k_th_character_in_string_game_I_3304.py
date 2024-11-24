import string


def kth_character(k: int) -> str:
    word = "a"
    while len(word) < k:
        for letter in word:
            index = string.ascii_lowercase.index(letter)
            new_index = index + 1
            word += string.ascii_lowercase[new_index]
    return word[k-1]
