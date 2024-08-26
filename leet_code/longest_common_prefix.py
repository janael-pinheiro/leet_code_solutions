from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    response = ""
    character_index = 0
    count = 0
    first_word = strs[0]
    while count < len(first_word):
        selected_character = first_word[character_index]
        for word in strs:
            if len(word) <= character_index:
                return response
            current_character = word[character_index]
            if selected_character != current_character:
                return response
        response += selected_character
        character_index += 1
        count += 1
    return response
