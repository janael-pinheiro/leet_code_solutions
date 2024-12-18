from leet_code.keys_and_rooms_841 import can_visit_all_rooms


from pytest import mark


@mark.parametrize("rooms, expected", [
    ([[1], [2], [3], []], True),
    ([[1, 3], [3, 0, 1], [2], [0]], False)
])
def test_can_visit_all_rooms(rooms, expected):
    output = can_visit_all_rooms(rooms)
    assert output == expected
