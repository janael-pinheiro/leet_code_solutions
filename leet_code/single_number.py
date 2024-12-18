from typing import List


def single_number(nums: List[int]) -> int:
    singles_numbers = set()
    for number in nums:
        if number in singles_numbers:
            singles_numbers.remove(number)
        else:
            singles_numbers.add(number)
    return singles_numbers.pop()
