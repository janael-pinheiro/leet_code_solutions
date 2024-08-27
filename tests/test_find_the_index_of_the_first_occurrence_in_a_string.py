from leet_code.find_the_index_of_the_first_occurrence_in_a_string import find
from pytest import mark


@mark.parametrize("haystack, needle, expected", [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("addeukd", "euk", 3),
    ("a", "a", 0)
])
def test_find(haystack, needle, expected):
    output = find(haystack, needle)
    assert output == expected
