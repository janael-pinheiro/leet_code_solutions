from leet_code.valid_parentheses import is_valid
from pytest import mark


@mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([])", True),
    ("[", False),
    ("((", False)
])
def test_is_valid(s, expected):
    output = is_valid(s)
    assert output == expected
