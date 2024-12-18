from leet_code.product_of_array_except_self import product_except_self
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
])
def test_product_except_self(nums, expected):
    output = product_except_self(nums)
    assert output == expected
