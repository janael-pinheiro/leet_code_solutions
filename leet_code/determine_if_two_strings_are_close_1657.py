from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    word1_counter = sorted(Counter(word1).values())
    word2_counter = sorted(Counter(word2).values())

    index = 0
    while index < len(word1_counter):
        if word1[index] not in word2 or word1_counter[index] != word2_counter[index]:
            return False
        index += 1

    return True
