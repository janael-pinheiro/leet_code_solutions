from leet_code.roman_to_integer import roman_to_int
from pytest import mark


@mark.parametrize("s, expected", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994)
])
def test_roman_to_int(s, expected):
    output = roman_to_int(s)
    assert expected == output
