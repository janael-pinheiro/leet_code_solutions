from leet_code.fibonacci_number import fib
from pytest import mark


@mark.parametrize("n, expected", [
    (2, 1),
    (1, 1),
    (0, 0),
    (3, 2),
    (4, 3)

])
def test_fib(n, expected):
    output = fib(n)
    assert expected == output
