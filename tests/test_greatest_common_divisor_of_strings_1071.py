from pytest import mark

from leet_code.greatest_common_divisor_of_strings_1071 import gcd_of_strings


@mark.parametrize("str1, str2, expected", [
    ("ABCABC", "ABC", "ABC"),
    ("ABABAB", "ABAB", "AB"),
    ("LEET", "CODE", ""),
    ("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXX")
])
def test_gcd_of_strings(str1, str2, expected):
    output = gcd_of_strings(str1, str2)
    assert expected == output
