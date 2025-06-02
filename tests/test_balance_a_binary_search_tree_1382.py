from leet_code.balance_a_binary_search_tree_1382 import Solution

from pytest import mark

@mark.parametrize("root, expected", [
    ([2, 1, 3], [2, 1, 3]),
    ([1, None, 2, None, 3, None, 4], [2, 1, 3, None, None, None, 4])
])
def test_balance_BST(root, expected, build_tree):
    solution = Solution()
    output = solution.balance_BST(build_tree(root))
    assert output == build_tree(expected)
