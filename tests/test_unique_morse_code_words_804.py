from leet_code.unique_morse_code_words_804 import unique_morse_representations

from pytest import mark


@mark.parametrize("words, expected", [
    (["gin", "zen", "gig", "msg"], 2),
    (["a"], 1)
])
def test_unique_morse_representations(words, expected):
    output = unique_morse_representations(words)
    assert expected == output
