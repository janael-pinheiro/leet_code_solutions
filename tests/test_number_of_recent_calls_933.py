from leet_code.number_of_recent_calls_933 import RecentCounter

from pytest import mark


@mark.parametrize("ping, expected", [
    ([1, 100, 3001, 3002], [1, 2, 3, 3])
])
def test_recent_counter(ping, expected):
    recent_counter = RecentCounter()
    for t, e in zip(ping, expected):
        output = recent_counter.ping(t)
        assert e == output
