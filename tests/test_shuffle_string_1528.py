from leet_code.shuffle_string_1528 import Solution

from pytest import mark


@mark.parametrize("s, indices, expected", [
    ("codeleet", [4, 5, 6, 7, 0, 2, 1, 3], "leetcode"),
    ("abc", [0, 1, 2], "abc")
])
def test_restore_string(s, indices, expected):
    solution = Solution()
    output = solution.restore_string(s, indices)
    assert expected == output
