from pytest import mark

from leet_code.keyboard_row_500 import find_words


@mark.parametrize("words, expected", [
    (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
    (["omk"], []),
    (["adsdf", "sfd"], ["adsdf", "sfd"])
])
def test_find_words(words, expected):
    output = find_words(words)
    assert expected == output
