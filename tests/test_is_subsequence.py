from leet_code.is_subsequence import is_subsequence
from pytest import mark


@mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False)
])
def test_is_subsequence(s, t, expected):
    output = is_subsequence(s, t)
    assert output == expected
