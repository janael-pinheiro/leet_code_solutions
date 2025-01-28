from leet_code.find_all_numbers_disappeared_in_an_array_448 import Solution


from pytest import mark


@mark.parametrize("nums, expected", [
    ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
    ([1, 1], [2])
])
def test_find_disappeared_numbers(nums, expected):
    solution = Solution()
    output = solution.find_disappeared_numbers(nums)
    assert output == expected
