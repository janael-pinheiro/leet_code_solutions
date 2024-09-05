from typing import List


def decimal_to_binary(value) -> List[int]:
    result = value
    response = []
    while result > 0:
        response.insert(0, result % 2)
        result = result // 2
    return response


def binary_to_decimal(value: str) -> int:
    return int(value, 2)


def pad_value(value: List[str]) -> List[str]:
    r = 32 - len(value)
    response = ["0"] * r
    response.extend(value)
    return response


def reverse_bits(n: int) -> int:
    reverse = ""
    binary_number = decimal_to_binary(n)
    input_pad = pad_value([str(x) for x in binary_number])
    index = len(input_pad) - 1
    while index >= 0:
        reverse += str(input_pad[index])
        index -= 1
    return binary_to_decimal(reverse)
