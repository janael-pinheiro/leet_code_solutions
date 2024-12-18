def is_happy(n: int) -> bool:
    if n == 1:
        return True
    elif 1 < n < 10:
        return False
    already_seen = {}
    total = 0
    current = n
    while total != 1:
        temp_total = 0
        while current // 10 > 0:
            digit = current % 10
            current = current // 10
            temp_total += digit ** 2
        digit = current % 10
        temp_total += digit ** 2
        total = temp_total
        current = total
        if current in already_seen:
            return False
        already_seen[current] = True
    return True
