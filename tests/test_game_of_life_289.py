from pytest import mark

from leet_code.game_of_life_289 import Solution


@mark.parametrize("board, expected", [
    ([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]], [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]),
    ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ([[0]], [[0]]),
    ([[1], [0], [0], [1], [0], [0], [1], [0], [0], [1]], [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]),
    ([[1], [0], [1], [1], [1], [0]], [[0], [0], [0], [1], [0], [0]])
])
def test_game_of_life(board, expected):
    solution = Solution()
    solution.game_of_life(board)
    assert board == expected
