from typing import List


def equal_pairs(grid: List[List[int]]) -> int:
    number_rows = len(grid)
    number_columns = len(grid[0])
    counter = {}
    number_of_pairs = 0

    column = 0
    while column < number_columns:
        result = []
        row = 0
        while row < number_rows:
            result.append(str(grid[row][column]))
            row += 1
        hashed_result = hash("-".join(result))
        current = counter.get(hashed_result, 0)
        counter[hashed_result] = current + 1
        column += 1

    row = 0
    while row < number_rows:
        result = []
        column = 0
        while column < number_columns:
            result.append(str(grid[row][column]))
            column += 1
        hashed_result = hash("-".join(result))
        if hashed_result in counter:
            number_of_pairs += counter[hashed_result]
        row += 1

    return number_of_pairs
