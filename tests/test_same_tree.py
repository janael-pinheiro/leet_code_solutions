from leet_code.same_tree import is_same_tree
from pytest import mark


@mark.parametrize("p, q, expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([1, None, 1], [1, None, 1], True)
])
def test_is_same_tree(p, q, expected, build_tree):
    p_tree = build_tree(p)
    q_tree = build_tree(q)
    output = is_same_tree(p_tree, q_tree)
    assert output == expected
