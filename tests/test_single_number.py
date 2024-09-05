from leet_code.single_number import single_number
from pytest import mark


@mark.parametrize("nums, expected", [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
])
def test_single_number(nums, expected):
    output = single_number(nums)
    assert output == expected
