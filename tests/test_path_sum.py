from leet_code.path_sum import has_path_sum
from pytest import mark


@mark.parametrize("nodes, target_sum, expected", [
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True),
    ([1, 2, 3], 5, False),
    ([], 0, False),
    ([1], 1, True),
    ([1, 2], 1, False),
    ([1, 2, None, 3, None, 4, None, 5], 6, False)
])
def test_has_path_sum(nodes, target_sum, expected, build_tree):
    input_tree = build_tree(nodes)
    output = has_path_sum(input_tree, target_sum)
    assert output == expected
