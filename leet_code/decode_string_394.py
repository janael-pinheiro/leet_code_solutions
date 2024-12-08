import string

from typing import List


def _get_multiplier(stack: List) -> int:
    multiplier = stack.pop(0)
    multi = 0
    m = 1
    while multiplier in string.digits:
        multi += int(multiplier) * m
        m = m * 10
        if len(stack) == 0:
            break
        multiplier = stack.pop(0)
    if multiplier not in string.digits:
        stack.insert(0, multiplier)
    return multi


def decode_string(s: str) -> str:
    response = []
    index = 0
    stack = []
    while index < len(s):
        if len(stack) == 0 and s[index] in string.ascii_lowercase:
            response.append(s[index])
            index += 1
            continue
        if len(stack) == 0:
            stack.insert(0, s[index])
            index += 1
            continue

        if s[index] == "]":
            current_string = []
            character = stack.pop(0)
            while character != "[":
                current_string.append(character)
                character = stack.pop(0)
            multi = _get_multiplier(stack)
            idx = 0
            if len(stack) == 0:
                while idx < int(multi):
                    response.extend(reversed(current_string))
                    idx += 1
            else:
                while idx < int(multi):
                    for letter in reversed(current_string):
                        stack.insert(0, letter)
                    idx += 1
        elif index == len(s) - 1:
            stack.insert(0, s[index])
            response.extend(reversed(stack))
        else:
            stack.insert(0, s[index])
        index += 1
    return "".join(response)
