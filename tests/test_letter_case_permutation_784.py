from pytest import mark

from leet_code.letter_case_permutation_784 import Solution


@mark.parametrize("s, expected", [
    ("a1b2", ["A1B2", "A1b2", "a1B2", "a1b2"]),
    ("3z4", ["3Z4", "3z4"])
])
def test_letter_case_permutation(s, expected):
    solution = Solution()
    output = solution.letter_case_permutation(s)
    assert expected == output
