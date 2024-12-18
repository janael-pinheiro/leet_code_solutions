from typing import Dict


def _get_tribonacci(n: int, index: int, memory: Dict[int, int]) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    memory[index] = memory[index - 1] + memory[index - 2] + memory[index - 3]
    if index == n:
        return memory[index]
    return _get_tribonacci(n, index+1, memory)


def tribonacci(n: int) -> int:
    memory = {0: 0, 1: 1, 2: 1}
    return _get_tribonacci(n, 3, memory)
