def find(haystack: str, needle: str) -> int:
    if len(haystack) < len(needle):
        return -1
    length_needle = len(needle)
    length_haystack = len(haystack)
    needle_hash = hash(needle)
    index = 0
    while index < length_haystack:
        if index+length_needle <= length_haystack:
            selected_substring = haystack[index:index+length_needle]
            if hash(selected_substring) == needle_hash:
                return index
        index += 1
    return -1
