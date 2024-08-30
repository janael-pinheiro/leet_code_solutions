from pytest import mark

from leet_code.maximum_depth_of_binary_tree import max_depth


@mark.parametrize("nodes, expected", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2)
])
def test_max_depth(nodes, expected, build_tree):
    input_tree = build_tree(nodes)
    output = max_depth(input_tree)
    assert output == expected
