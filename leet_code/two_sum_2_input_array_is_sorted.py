from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    i, j = 0, 1
    while i < len(numbers) and j < len(numbers):
        query = target - numbers[i]
        while j < len(numbers) and numbers[j] < query:
            if numbers[j] == numbers[i]:
                i += 1
            j += 1
        if j < len(numbers) and numbers[j] == query:
            return [i + 1, j + 1]
        i += 1
        j = i + 1
