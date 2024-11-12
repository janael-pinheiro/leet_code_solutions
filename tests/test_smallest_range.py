from leet_code.smallest_range import smallest_range
from pytest import mark


@mark.parametrize("nums, k, expected", [
    ([1], 0, 0),
    ([0, 10], 2, 6),
    ([1, 3, 6], 3, 0)
])
def test_smallest_range(nums, k, expected):
    output = smallest_range(nums, k)
    assert expected == output
