package solutions

import com.leet_code.solutions.Solution
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.params.ParameterizedTest
import org.junit.jupiter.params.provider.Arguments
import org.junit.jupiter.params.provider.MethodSource

class TestMergeStringsAlternately1768 {
    @ParameterizedTest
    @MethodSource("words")
    fun testMergeAlternately(word1: String, word2: String, expected: String){
        val solution = Solution()
        val actual = solution.mergeAlternately(word1, word2)
        assertEquals(expected, actual)
    }

    companion object {
        @JvmStatic
        fun words() = listOf(
            Arguments.of("abc", "pqr", "apbqcr"),
            Arguments.of("ab", "pqrs", "apbqrs"),
            Arguments.of("abcd", "pq", "apbqcd"),
        )
    }
}