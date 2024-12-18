from leet_code.longest_substring_without_repeating_characters import length_of_longest_substring
from pytest import mark


@mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3)
])
def test_length_of_longest_substring(s, expected):
    output = length_of_longest_substring(s)
    assert output == expected
