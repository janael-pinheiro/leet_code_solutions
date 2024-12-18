from pytest import mark

from leet_code.asteroid_collision_735 import asteroid_collision


@mark.parametrize("asteroids, expected", [
    ([1, -2, -2, -2], [-2, -2, -2]),
    ([8, -8], []),
    ([-2, -2, 1, -2], [-2, -2, -2]),
    ([5, 10, -5], [5, 10]),
    ([10, 2, -5], [10]),
    ([-2, -1, 1, 2], [-2, -1, 1, 2])
])
def test_asteroid_collision(asteroids, expected):
    output = asteroid_collision(asteroids)
    assert expected == output
