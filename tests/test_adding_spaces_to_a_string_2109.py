from pytest import mark

from leet_code.adding_spaces_to_a_string_2109 import add_spaces


@mark.parametrize("s, spaces, expected", [
    ("LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"),
    ("icodeinpython", [1, 5, 7, 9], "i code in py thon"),
    ("spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g")
])
def test_add_spaces(s, spaces, expected):
    output = add_spaces(s, spaces)
    assert expected == output
