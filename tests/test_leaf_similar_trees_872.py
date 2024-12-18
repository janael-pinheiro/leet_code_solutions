from pytest import mark

from leet_code.leaf_similar_trees_872 import leaf_similar


@mark.parametrize("root1, root2, expected", [
    ([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4], [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8], True),
    ([1, 2, 3], [1, 3, 2], False)
])
def test_leaf_similar(root1, root2, expected, build_tree):
    output = leaf_similar(build_tree(root1), build_tree(root2))
    assert expected == output
