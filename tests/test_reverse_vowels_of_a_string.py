from leet_code.reverse_vowels_of_a_string import reverse_vowels
from pytest import mark


@mark.parametrize("s, expected", [
    ("IceCreAm", "AceCreIm"),
    ("leetcode", "leotcede")
])
def test_reverse_vowels(s, expected):
    output = reverse_vowels(s)
    assert expected == output
