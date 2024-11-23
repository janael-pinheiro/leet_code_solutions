from leet_code.reverse_words_in_a_string_151 import reverse_words
from pytest import mark


@mark.parametrize("s, expected", [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a")
])
def test_reverse_words(s, expected):
    output = reverse_words(s)
    assert expected == output
