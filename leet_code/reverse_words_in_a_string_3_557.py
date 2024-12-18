def reverse_words(s: str) -> str:
    words = s.split(" ")
    output_words = []
    for word in words:
        letters = [w for w in word]
        left = 0
        right = len(letters) - 1
        while left < right:
            temp = letters[left]
            letters[left] = letters[right]
            letters[right] = temp
            left += 1
            right -= 1
        output_words.append("".join(letters))
    return " ".join(output_words)
