from typing import List


def plus_one(digits: List[int]) -> List[int]:
    last = len(digits) - 1
    updated_digits = list(digits)
    if digits[last] != 9:
        updated_digits[last] = updated_digits[last] + 1
    else:
        while digits[last] == 9 and last >= 0:
            updated_digits[last] = 0
            last -= 1
            if last >= 0:
                updated_digits[last] = updated_digits[last] + 1
            else:
                updated_digits.insert(0, 1)
    return updated_digits
