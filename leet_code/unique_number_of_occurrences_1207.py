from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    counter = {}
    for number in arr:
        count = counter.get(number, 0)
        count += 1
        counter[number] = count
    counters = counter.values()
    return len(set(counters)) == len(counters)
