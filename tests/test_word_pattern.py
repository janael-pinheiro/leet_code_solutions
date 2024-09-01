from leet_code.word_pattern import word_pattern
from pytest import mark


@mark.parametrize("pattern, s, expected", [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog cat cat fish", False),
    ("aaaa", "dog cat cat fish", False),
    ("abba", "dog dog dog dog", False)
])
def test_word_pattern(pattern, s, expected):
    output = word_pattern(pattern, s)
    assert output == expected
