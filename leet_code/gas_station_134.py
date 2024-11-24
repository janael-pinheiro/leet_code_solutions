from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return - 1
    index = 0
    diff = []
    while index < len(gas):
        diff.append(gas[index] - cost[index])
        index += 1

    index = 0
    start = 0
    total = 0
    while index < len(gas):
        total += diff[index]
        if total < 0:
            start = index + 1
            total = 0
        index += 1
    return start
