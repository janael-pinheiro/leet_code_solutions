package com.leet_code.solutions

class Solution {
    fun mergeAlternately(word1: String, word2: String): String {
        var i = 0
        var j = 0
        var result = ""
        while (i < word1.length && j < word2.length) {
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        }

        while (i < word1.length ) {
            result += word1[i]
            i += 1
        }

        while (j < word2.length) {
            result += word2[j]
            j += 1
        }
        return result
    }
}