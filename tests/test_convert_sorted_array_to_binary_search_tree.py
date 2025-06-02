from leet_code.convert_sorted_array_to_binary_search_tree import Solution


from pytest import mark

@mark.parametrize("nums, expected", [
    ([-10, -3, 0, 5, 9], [0, -10, 5, None, -3, None, 9]),
    ([1, 3], [1, None, 3])
])
def test_sorted_array_to_BST(nums, expected, build_tree):
    solution = Solution()
    output = solution.sorted_array_to_BST(nums)
    assert output == build_tree(expected)
