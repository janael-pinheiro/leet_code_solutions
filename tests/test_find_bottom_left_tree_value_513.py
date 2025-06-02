from pytest import mark

from leet_code.find_bottom_left_tree_value_513 import Solution


@mark.parametrize("root, expected", [
    ([2, 1, 3], 1),
    ([1, 2, 3, 4, None, 5, 6, None, None, 7], 7)
])
def test_find_bottom_left_value(root, expected, build_tree):
    solution = Solution()
    output = solution.find_bottom_left_value(build_tree(root))
    assert output == expected
