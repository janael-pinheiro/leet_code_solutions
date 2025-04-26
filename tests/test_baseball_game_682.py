from pytest import mark
from leet_code.baseball_game_682 import Solution


@mark.parametrize("operations, expected", [
    (["5", "2", "C", "D", "+"], 30),
    (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    (["1", "C"], 0)
])
def test_cal_points(operations, expected):
    solution = Solution()
    output = solution.cal_points(operations)
    assert expected == output
