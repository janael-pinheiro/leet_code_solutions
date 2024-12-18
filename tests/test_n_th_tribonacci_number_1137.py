from pytest import mark

from leet_code.n_th_tribonacci_number_1137 import tribonacci


@mark.parametrize("n, expected", [
    (4, 4),
    (25, 1389537)
])
def test_tribonacci(n, expected):
    output = tribonacci(n)
    assert expected == output
