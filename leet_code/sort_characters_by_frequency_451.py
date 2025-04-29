class Solution:
    def frequency_sort(self, s: str) -> str:
        frequency = {}
        for letter in s:
            freq = frequency.get(letter, 0)
            frequency[letter] = freq + 1
        sorted_frequencies = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        result = []
        for freq in sorted_frequencies:
            for _ in range(freq[1]):
                result.append(freq[0])
        return "".join(result)
