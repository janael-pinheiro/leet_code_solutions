from leet_code.binary_tree_right_side_view_199 import right_side_view

from pytest import mark


@mark.parametrize("root, expected", [
    ([1, None, 4, 3, 5, 2, None, None, 6], [1, 4, 5, 6]),
    ([6, 1, None, None, 3, 2, 5, None, None, 4], [6, 1, 3, 5, 4]),
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
    ([1, None, 3], [1, 3]),
    ([], [])
])
def test_right_side_view(root, expected, build_tree):
    output = right_side_view(build_tree(root))
    assert output == expected
