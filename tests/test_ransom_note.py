from leet_code.ransom_note import can_construct
from pytest import mark


@mark.parametrize("ransom_note, magazine, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True)
])
def test_can_construct(ransom_note, magazine, expected):
    output = can_construct(ransom_note, magazine)
    assert output == expected
