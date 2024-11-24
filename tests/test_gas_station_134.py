from leet_code.gas_station_134 import can_complete_circuit
from pytest import mark


@mark.parametrize("gas, cost, expected", [
    ([5, 8, 2, 8], [6, 5, 6, 6], 3),
    ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),
    ([3, 1, 1], [1, 2, 2], 0),
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1)
])
def test_can_complete_circuit(gas, cost, expected):
    output = can_complete_circuit(gas, cost)
    assert output == expected
