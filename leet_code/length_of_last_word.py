def length_of_last_word(s: str) -> int:
    last_word = s.strip().split(" ")[-1]
    return len(last_word)
