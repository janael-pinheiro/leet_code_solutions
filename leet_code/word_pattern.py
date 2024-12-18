def word_pattern(pattern: str, s: str) -> bool:
    words = s.split(" ")
    if len(pattern) != len(words):
        return False
    pattern_index = {}
    for index, p in enumerate(pattern):
        mapping = pattern_index.get(p, [])
        mapping.append(index)
        pattern_index[p] = mapping
    for _, indexes in pattern_index.items():
        base = hash(words[indexes[0]])
        for index, word in enumerate(words):
            if index not in indexes and hash(word) == base:
                return False
            elif index in indexes and hash(word) != base:
                return False
    return True
