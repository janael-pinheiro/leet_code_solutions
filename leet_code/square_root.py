def square_root(x: int) -> int:
    if x == 0:
        return 0
    y = 2
    while y ** 2 < x:
        y += 1
    if y ** 2 > x:
        return y - 1
    return y
