from leet_code.letter_combinations_of_a_phone_number_17 import Solution

from pytest import mark

@mark.parametrize("digits, expected", [
    ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
    ("", []),
    ("2", ["a","b","c"]),
    ("8", ["t", "u", "v"])
])
def test_letter_combinations(digits, expected):
    solution = Solution()
    output = solution.letter_combinations(digits)
    assert expected == output
