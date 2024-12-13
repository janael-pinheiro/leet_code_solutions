from pytest import mark

from leet_code.find_peak_element_162 import find_peak_element


@mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], 2),
    ([1, 2, 1, 3, 5, 6, 4], 5)
])
def test_find_peak_element(nums, expected):
    output = find_peak_element(nums)
    assert expected == output
