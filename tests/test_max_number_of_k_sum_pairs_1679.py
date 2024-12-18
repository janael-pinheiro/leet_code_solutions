from leet_code.max_number_of_k_sum_pairs_1679 import max_operations

from pytest import mark


@mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4], 5, 2),
    ([3, 1, 3, 4, 3], 6, 1)
])
def test_max_operations(nums, k, expected):
    output = max_operations(nums, k)
    assert expected == output
