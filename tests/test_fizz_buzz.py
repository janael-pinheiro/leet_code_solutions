from leet_code.fizz_buzz import fizz_buzz
from pytest import mark


@mark.parametrize("n, expected", [
    (3, ["1", "2", "Fizz"]),
    (5, ["1", "2", "Fizz", "4", "Buzz"]),
    (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"])
])
def test_fizz_buzz(n, expected):
    output = fizz_buzz(n)
    assert expected == output
