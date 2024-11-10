def reverse_vowels(s: str) -> str:
    input_string = [x for x in s]
    left = 0
    right = len(s) - 1
    vowels = "aeiouAEIOU"
    while left < right:
        if input_string[left] in vowels and input_string[right] in vowels:
            temp = input_string[left]
            input_string[left] = input_string[right]
            input_string[right] = temp
            left += 1
            right -= 1
        elif input_string[left] in vowels:
            right -= 1
        elif input_string[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1

    return "".join(input_string)
