from typing import List


def max_profit(prices: List[int]) -> int:
    current = prices[0]
    response = 0
    index = 1
    while index < len(prices):
        if prices[index] > current:
            difference = prices[index] - current
            if difference > response:
                response = difference
        elif prices[index] < current:
            current = prices[index]
        index += 1
    return response

