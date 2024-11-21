from typing import List


def compress(chars: List[str]) -> int:
    left = 0
    while left < len(chars):
        right = left + 1
        group_length = 1
        while right < len(chars) and chars[left] == chars[right]:
            group_length += 1
            chars.pop(right)
        if group_length > 1:
            left = right
            if group_length >= 10:
                move = 0
                while group_length // 10 > 0:
                    chars.insert(left, str(group_length % 10))
                    group_length = group_length // 10
                    move += 1
                chars.insert(left, str(group_length % 10))
                move += 1
                left += move
            else:
                chars.insert(left, str(group_length))
                left += 1
        else:
            left += 1
    return len(chars)
