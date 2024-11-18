from leet_code.find_the_difference_of_two_arrays import find_difference

from pytest import mark


@mark.parametrize("nums1, nums2, expected", [
    ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
    ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []])
])
def test_find_difference(nums1, nums2, expected):
    output = find_difference(nums1, nums2)
    assert expected == output
