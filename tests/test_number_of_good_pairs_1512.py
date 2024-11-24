from leet_code.number_of_good_pairs_1512 import num_identical_pairs
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0)
])
def test_num_identical_pairs(nums, expected):
    output = num_identical_pairs(nums)
    assert expected == output
