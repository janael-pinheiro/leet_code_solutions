def get_symbol(num, multiplier, mapping):
    if num * multiplier in mapping:
        return mapping[num * multiplier]
    elif multiplier < 1000 and num * multiplier > 5 * multiplier:
        return mapping[5 * multiplier] + mapping[multiplier] * (num - 5)
    elif multiplier < 1000 and num * multiplier < 5 * multiplier:
        return mapping[multiplier] * num
    else:
        m = mapping[multiplier]
        return m * num


def convert_integer_to_list(num: int, multiplier, mapping) -> str:
    if num // 10 == 0:
        return get_symbol(num, multiplier, mapping)
    symbol = convert_integer_to_list(num // 10, multiplier * 10, mapping)
    decimal = (num % 10)
    return symbol + get_symbol(decimal, multiplier, mapping)


def int_to_roman(num: int) -> str:
    integer_to_roman_mapping = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        3: "III",
        2: "II",
        1: "I"
    }
    return convert_integer_to_list(num, 1, integer_to_roman_mapping)
