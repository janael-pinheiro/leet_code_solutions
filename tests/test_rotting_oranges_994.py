from pytest import mark

from leet_code.rotting_oranges_994 import Solution


@mark.parametrize("grid, expected", [
    ([[2, 1, 1], [1, 1, 1], [0, 1, 2]], 2),
    ([[0, 0, 0, 0]], 0),
    ([[0, 1]], -1),
    ([[0]], 0),
    ([[1]], -1),
    ([[2]], 0),
    ([[0, 2]], 0),
    ([[2, 0]], 0),
    ([[0, 2, 1]], 1),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
])
def test_oranges_rotting(grid, expected):
    solution = Solution()
    output = solution.oranges_rotting(grid)
    assert expected == output
