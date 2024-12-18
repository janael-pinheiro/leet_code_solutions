import string
from typing import List


def unique_morse_representations(words: List[str]) -> int:
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                  "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    letter_morse_code_mapping = {letter: code for letter, code in zip(string.ascii_lowercase, morse_code)}
    result = {}
    for word in words:
        transformed_word = "".join([letter_morse_code_mapping[letter] for letter in word])
        result[transformed_word] = True
    return len(result)
