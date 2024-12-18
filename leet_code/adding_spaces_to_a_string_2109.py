from typing import List


def add_spaces(s: str, spaces: List[int]) -> str:
    response = ""
    idx = 0
    current = 0
    while len(spaces) > 0:
        current = spaces.pop(0)
        response += s[idx:current]
        response += " "
        idx = current
    return response + s[current:]
