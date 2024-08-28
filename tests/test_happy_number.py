from leet_code.happy_number import is_happy
from pytest import mark


@mark.parametrize("n, expected", [
    (2, False),
    (19, True),
    (99, False)
])
def test_is_happy(n, expected):
    output = is_happy(n)
    assert output == expected
