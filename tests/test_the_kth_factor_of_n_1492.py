from leet_code.the_kth_factor_of_n_1492 import Solution
from pytest import mark


@mark.parametrize("n, k, expected", [
    (12, 3, 3),
    (7, 2, 7),
    (4, 4, -1)
])
def test_kth_factor(n, k, expected):
    solution = Solution()
    output = solution.kthFactor(n, k)
    assert output == expected
