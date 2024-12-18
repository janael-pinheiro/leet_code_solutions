from leet_code.reverse_string import reverse_string
from pytest import mark


@mark.parametrize("s, expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
])
def test_reverse_string(s, expected):
    reverse_string(s)
    assert expected == s

