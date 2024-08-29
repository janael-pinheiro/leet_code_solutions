from leet_code.best_time_to_buy_and_sell_stock import max_profit
from pytest import mark


@mark.parametrize("prices, expected", [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0)
])
def test_max_profit(prices, expected):
    output = max_profit(prices)
    assert output == expected