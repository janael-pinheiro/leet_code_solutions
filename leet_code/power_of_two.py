def _power_of_two(n: int, current: int):
    if current > n:
        return False
    if current == n:
        return True
    return _power_of_two(n, current*2)


def is_power_of_two(n: int) -> bool:
    if n == 1:
        return True
    return _power_of_two(n, 2)
