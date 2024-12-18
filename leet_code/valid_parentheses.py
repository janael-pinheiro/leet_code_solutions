def is_valid(s: str) -> bool:
    valid = False
    character_mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    stack = []
    stack.insert(0, s[0])
    for character in s[1:]:
        try:
            c = stack.pop(0)
        except IndexError:
            stack.insert(0, character)
            continue
        if character in character_mapping and c != character_mapping[character]:
            return False
        if character not in character_mapping:
            stack.insert(0, c)
            stack.insert(0, character)
    if len(stack) == 0:
        return True
    return valid
