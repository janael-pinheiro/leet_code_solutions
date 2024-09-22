from leet_code.maximum_size_subarray_sum import min_subarray_sum
from pytest import mark


@mark.parametrize("target, nums, expected", [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)
])
def test_min_subarray_sum(target, nums, expected):
    output = min_subarray_sum(target, nums)
    assert output == expected
