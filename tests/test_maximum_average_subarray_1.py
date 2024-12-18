from leet_code.maximum_average_subarray_1 import find_max_average
from pytest import mark


@mark.parametrize("nums, k, expected", [
    ([1, 12, -5, -6, 50, 3], 4, 12.75000),
    ([5], 1, 5.00000)
])
def test_find_max_average(nums, k, expected):
    output = find_max_average(nums, k)
    assert expected == output
