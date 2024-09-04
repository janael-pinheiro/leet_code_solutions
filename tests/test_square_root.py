from leet_code.square_root import square_root
from pytest import mark


@mark.parametrize("x, expected", [
    (4, 2),
    (8, 2),
    (0, 0)
])
def test_square_root(x, expected):
    output = square_root(x)
    assert output == expected
