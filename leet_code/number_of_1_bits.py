from typing import List


def decimal_to_binary(value) -> List[int]:
    result = value
    response = []
    while result > 0:
        response.insert(0, result % 2)
        result = result // 2
    return response


def hamming_weight(n: int) -> int:
    binary_number = decimal_to_binary(n)
    return sum(binary_number)
