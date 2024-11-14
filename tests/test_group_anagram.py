from leet_code.group_anagrams import group_anagrams
from pytest import mark


@mark.parametrize("s, expected", [
    ([""], [[""]]),
    (["a"], [["a"]]),
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
])
def test_group_anagrams(s, expected):
    output = group_anagrams(s)
    assert expected == output
