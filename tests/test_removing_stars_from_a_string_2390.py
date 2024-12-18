from pytest import mark

from leet_code.removing_stars_from_a_string_2390 import remove_stars


@mark.parametrize("s, expected", [
    ("leet**cod*e", "lecoe"),
    ("erase*****", "")
])
def test_remove_stars(s, expected):
    output = remove_stars(s)
    assert expected == output
