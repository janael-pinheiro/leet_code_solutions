from typing import List


def max_profit(prices: List[int]) -> int:
    index = 0
    profit = 0
    while index + 1 < len(prices):
        current = prices[index]
        c = current
        while index < len(prices) - 1 and c < prices[index + 1]:
            c = prices[index + 1]
            index += 1
        difference = prices[index] - current
        if difference > 0:
            profit += difference
        index += 1
    return profit
