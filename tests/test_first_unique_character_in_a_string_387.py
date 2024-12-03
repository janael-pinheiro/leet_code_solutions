from leet_code.first_unique_character_in_a_string_387 import first_unique_character

from pytest import mark


@mark.parametrize("s, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1)
])
def test_first_unique_character(s, expected):
    output = first_unique_character(s)
    assert expected == output
