from pytest import mark

from leet_code.minimum_depth_binary_tree import min_depth


@mark.parametrize("root, expected", [
    ([3, 9, 20, None, None, 15, 7], 2),
    ([2, None, 3, None, 4, None, 5, None, 6], 5)
])
def test_min_depth(root, expected, build_tree):
    output = min_depth(build_tree(root))
    assert expected == output
