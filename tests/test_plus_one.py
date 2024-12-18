from leet_code.plus_one import plus_one
from pytest import mark


@mark.parametrize("digits, expected", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([1, 9], [2, 0])
])
def test_plus_one(digits, expected):
    output = plus_one(digits)
    assert output == expected
