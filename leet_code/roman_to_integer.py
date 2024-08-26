def roman_to_int(s: str) -> int:
    roman_to_integer_mapping = {
        hash("I"): 1,
        hash("V"): 5,
        hash("X"): 10,
        hash("L"): 50,
        hash("C"): 100,
        hash("D"): 500,
        hash("M"): 1000,
        hash("IV"): 4,
        hash("IX"): 9,
        hash("XL"): 40,
        hash("XC"): 90,
        hash("CD"): 400,
        hash("CM"): 900
    }
    response = 0
    index = 0
    n = len(s)
    while index < n:
        current_value = s[index]
        if index < n - 1:
            next_value = s[index + 1]
            if hash(current_value + next_value) not in roman_to_integer_mapping:
                response += roman_to_integer_mapping[hash(current_value)]
            else:
                response += roman_to_integer_mapping[hash(current_value + next_value)]
                index += 1
        else:
            response += roman_to_integer_mapping[hash(current_value)]
        index += 1
    return response
