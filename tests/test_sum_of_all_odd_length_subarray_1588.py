from leet_code.sum_of_all_odd_length_subarray_1588 import sum_odd_length_sub_arrays
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 4, 2, 5, 3], 58),
    ([1, 2], 3),
    ([10, 11, 12], 66)
])
def test_sum_odd_length_sub_arrays(nums, expected):
    output = sum_odd_length_sub_arrays(nums)
    assert expected == output
