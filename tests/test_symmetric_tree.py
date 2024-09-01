from leet_code.symmetric_tree import is_symmetric
from pytest import mark


@mark.parametrize("nodes, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False),
    ([1], True),
    ([], False),
    ([1, 2, 2, None, 3, 3], True)
])
def test_is_symmetric(nodes, expected, build_tree):
    root_tree = build_tree(nodes)
    output = is_symmetric(root_tree)
    assert output == expected
