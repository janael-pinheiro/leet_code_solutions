from leet_code.jump_game import can_jump
from pytest import mark


@mark.parametrize("nums, expected", [
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False)
])
def test_can_jump(nums, expected):
    output = can_jump(nums)
    assert output == expected
