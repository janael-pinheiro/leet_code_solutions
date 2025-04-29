from pytest import mark

from leet_code.sort_characters_by_frequency_451 import Solution


@mark.parametrize("s, expected", [
    ("tree", "eetr"),
    ("cccaaa", "cccaaa"),
    ("Aabb", "bbAa")
])
def test_frequency_sort(s, expected):
    solution = Solution()
    output = solution.frequency_sort(s)
    assert expected == output
