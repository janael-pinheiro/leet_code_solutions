from leet_code.remove_duplicates_from_sorted_array import remove_duplicates
from pytest import mark


@mark.parametrize("nums, expected", [
    ([1, 1, 2], ([1, 2], 2)),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], ([[0, 1, 2, 3, 4], 5]))
])
def test_remove_duplicates(nums, expected):
    output = remove_duplicates(nums)
    assert nums == expected[0]
    assert output == expected[1]
