from leet_code.count_the_number_of_consistent_strings_1684 import Solution

from pytest import mark


@mark.parametrize("allowed, words, expected", [
    ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
    ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
    ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4)
])
def test_count_consistent_strings(allowed, words, expected):
    solution = Solution()
    output = solution.count_consistent_strings(allowed, words)
    assert output == expected
