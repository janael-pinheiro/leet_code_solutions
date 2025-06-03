from pytest import mark

from leet_code.create_binary_tree_from_descriptions_2196 import Solution


@mark.parametrize("descriptions, expected", [
    ([[1, 2, 1], [2, 3, 0], [3, 4, 1]], [1, 2, None, None, 3, 4]),
    ([[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]], [50, 20, 80, 15, 17, 19])
])
def test_create_binary_tree(descriptions, expected, build_tree):
    solution = Solution()
    output = solution.create_binary_tree(descriptions)
    assert output == build_tree(expected)
