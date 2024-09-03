from leet_code.rotate_array import rotate
from pytest import mark


@mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
    ([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1], 0, [1])
])
def test_rotate(nums, k, expected):
    rotate(nums, k)
    assert nums == expected
