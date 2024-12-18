from leet_code.majority_element import majority_element
from pytest import mark


@mark.parametrize("nums, expected", [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2)
])
def test_majority_element(nums, expected):
    output = majority_element(nums)
    assert expected == output
