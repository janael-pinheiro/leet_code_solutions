from pytest import mark

from leet_code.dota_2_senate_649 import predict_party_victory


@mark.parametrize("senate, expected", [
    ("DDDDRRDDDRDRDRRDDRDDDRDRRRRDRRRRRDRDDRDDRRDDRRRDDRRRDDDDRRRRRRRDDRRRDDRDDDRRRDRDDRDDDRRDRRDRRRDRDRDR", "Dire"),
    ("RD", "Radiant"),
    ("RDD", "Dire")
])
def test_predict_party_victory(senate, expected):
    output = predict_party_victory(senate)
    assert output == expected
