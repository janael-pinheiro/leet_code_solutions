from leet_code.combination_sum_40 import Solution


from pytest import mark


@mark.parametrize("candidates, target, expected", [
    ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
])
def test_combination_sum2(candidates, target, expected):
    solution = Solution()
    output = solution.combination_sum2(candidates, target)
    assert output == expected
