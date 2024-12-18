from pytest import mark

from leet_code.count_good_nodes_in_binary_tree_1448 import good_nodes


@mark.parametrize("root, expected", [
    ([3, 1, 4, 3, None, 1, 5], 4),
    ([3, 3, None, 4, 2], 3)
])
def test_good_nodes(root, expected, build_tree):
    output = good_nodes(build_tree(root))
    assert output == expected
