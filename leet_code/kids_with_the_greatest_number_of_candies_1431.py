from typing import List


def kids_with_candies(candies: List[int], extra_candies: int) -> List[bool]:
    max_candies = max(candies)
    result = [False for _ in range(len(candies))]
    index = 0
    while index < len(candies):
        if candies[index] + extra_candies >= max_candies:
            result[index] = True
        index += 1
    return result
