from leet_code.jump_game_2 import jump
from pytest import mark


@mark.parametrize("nums, expected", [
    ([2, 1, 1, 1, 1], 3),
    ([1, 2, 1, 1, 1], 3),
    ([1, 2, 3], 2),
    ([2, 3, 0, 1, 4], 2),
    ([2, 3, 1, 1, 4], 2)
])
def test_jump(nums, expected):
    output = jump(nums)
    assert output == expected
