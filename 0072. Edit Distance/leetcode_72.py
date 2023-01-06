from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)

        @lru_cache(None)
        def rec(i, j):
            if i >= len1:
                return len2 - j
            if j >= len2:
                return len1 - i
            while word1[i] == word2[j]:
                return rec(i + 1, j + 1)
            return min(rec(i, j + 1), rec(i + 1, j), rec(i + 1, j + 1)) + 1

        return rec(0, 0)
