from leet_code.valid_anagram import is_anagram
from pytest import mark


@mark.parametrize("s, t, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("ab", "a", False)
])
def test_is_anagram(s, t, expected):
    output = is_anagram(s, t)
    assert output == expected
