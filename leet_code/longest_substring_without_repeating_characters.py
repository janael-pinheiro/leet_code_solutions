def length_of_longest_substring(s: str) -> int:
    left, right = 0, 0
    longest_substring = 0
    substring = []
    while left < len(s) and right < len(s):
        if s[right] not in substring:
            substring.append(s[right])
            right += 1
        else:
            longest = right - left
            if longest > longest_substring:
                longest_substring = longest
            while s[right] in substring:
                left += 1
                substring.pop(0)
    longest = right - left
    if longest > longest_substring:
        longest_substring = longest
    return longest_substring
