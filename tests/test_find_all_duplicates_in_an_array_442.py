from pytest import mark

from leet_code.find_all_duplicates_in_an_array_442 import Solution


@mark.parametrize("nums, expected", [
    ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
    ([1, 1, 2], [1]),
    ([1], [])
])
def test_find_duplicates(nums, expected):
    solution = Solution()
    output = solution.find_duplicates(nums)
    assert expected == output
