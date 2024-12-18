from leet_code.increasing_triplet_subsequence_334 import increasing_triplet

from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 5, 0, 4, 1, 3], True),
    ([6, 7, 1, 2], False),
    ([1, 2, 3, 4, 5], True),
    ([2, 1, 5, 0, 4, 6], True),
    ([5, 4, 3, 2, 1], False)
])
def test_increasing_triplet(nums, expected):
    output = increasing_triplet(nums)
    assert expected == output
