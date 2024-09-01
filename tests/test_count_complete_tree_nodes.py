from leet_code.count_complete_tree_nodes import count_nodes
from pytest import mark


@mark.parametrize("nodes, expected", [
    ([1, 2, 3, 4, 5, 6], 6),
    ([], 0),
    ([1], 1)
])
def test_count_nodes(nodes, expected, build_tree):
    root = build_tree(nodes)
    output = count_nodes(root)
    assert output == expected
