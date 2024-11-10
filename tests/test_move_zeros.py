from leet_code.move_zeros import move_zeros

from pytest import mark


@mark.parametrize("nums, expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0]),
    ([0, 0, 1], [1, 0, 0])
])
def test_move_zeros(nums, expected):
    move_zeros(nums)
    assert expected == nums
