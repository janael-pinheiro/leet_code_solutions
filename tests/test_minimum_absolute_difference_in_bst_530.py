from leet_code.minimum_absolute_difference_in_bst_530 import Solution


from pytest import mark


@mark.parametrize("root, expected", [
    ([4, 2, 6, 1, 3], 1),
    ([1, 0, 48, None, None, 12, 49], 1)
])
def test_minimum_absolute_difference_in_bst(root, expected, build_tree):
    solution = Solution()
    output = solution.get_minimum_difference(build_tree(root))
    assert output == expected
