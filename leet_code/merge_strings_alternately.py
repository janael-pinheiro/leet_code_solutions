def merge_alternately(word1: str, word2: str) -> str:
    word_1_index = 0
    word_2_index = 0
    response = ""
    while word_1_index < len(word1) and word_2_index < len(word2):
        response += word1[word_1_index]
        response += word2[word_2_index]
        word_1_index += 1
        word_2_index += 1

    while word_1_index < len(word1):
        response += word1[word_1_index]
        word_1_index += 1

    while word_2_index < len(word2):
        response += word2[word_2_index]
        word_2_index += 1

    return response
