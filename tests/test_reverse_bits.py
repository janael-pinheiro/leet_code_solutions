from leet_code.reverse_bits import reverse_bits
from pytest import mark


@mark.parametrize("n, expected", [
    (43261596, 964176192),
    (4294967293, 3221225471)
])
def test_reverse_bits(n, expected):
    output = reverse_bits(n)
    assert output == expected
