from pytest import mark

from leet_code.longest_subarray_of_1_after_deleting_one_element_1493 import longest_subarray


@mark.parametrize("nums, expected", [
    ([1, 1, 0, 1], 3),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
    ([1, 1, 1], 2)
])
def test_longest_subarray(nums, expected):
    output = longest_subarray(nums)
    assert expected == output
