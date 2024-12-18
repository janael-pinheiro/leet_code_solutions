from pytest import mark

from leet_code.determine_if_two_strings_are_close_1657 import close_strings


@mark.parametrize("word1, word2, expected", [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True)
])
def test_close_strings(word1, word2, expected):
    output = close_strings(word1, word2)
    assert expected == output
