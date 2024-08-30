from leet_code.valid_palindrome import is_palindrome
from pytest import mark


@mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True)
])
def test_is_palindrome(s, expected):
    output = is_palindrome(s)
    assert output == expected
