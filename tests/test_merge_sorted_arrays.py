from leet_code.merge_sorted_arrays import merge
from pytest import mark


@mark.parametrize("nums1, m, nums2, n, expected", [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6])
])
def test_merge(nums1, m, nums2, n, expected):
    merge(nums1, m, nums2, n)
    assert nums1 == expected
