from leet_code.power_of_two import is_power_of_two
from pytest import mark


@mark.parametrize("n, expected", [
    (1, True),
    (16, True),
    (3, False),
    (128, True),
    (255, False),
    (511, False),
    (1024, True)
])
def test_is_power_of_two(n, expected):
    output = is_power_of_two(n)
    assert expected == output
