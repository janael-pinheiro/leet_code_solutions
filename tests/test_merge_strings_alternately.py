from leet_code.merge_strings_alternately import merge_alternately
from pytest import mark


@mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd")
])
def test_merge_alternately(word1, word2, expected):
    output = merge_alternately(word1, word2)
    assert expected == output
