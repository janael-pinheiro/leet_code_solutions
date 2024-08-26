from leet_code.longest_common_prefix import longest_common_prefix
from pytest import mark


@mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], "")
])
def test_longest_common_prefix(strs, expected):
    output = longest_common_prefix(strs)
    assert output == expected
