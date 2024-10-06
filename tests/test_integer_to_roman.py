from leet_code.integer_to_roman import int_to_roman
from pytest import mark


@mark.parametrize("num, expected", [
    (34, "XXXIV"),
    (20, "XX"),
    (60, "LX"),
    (111, "CXI"),
    (2, "II"),
    (3, "III"),
    (6, "VI"),
    (4, "IV"),
    (9, "IX"),
    (1994, "MCMXCIV"),
    (58, "LVIII"),
    (3749, "MMMDCCXLIX")
])
def test_convert_integer_to_list(num, expected):
    output = int_to_roman(num)
    assert output == expected
