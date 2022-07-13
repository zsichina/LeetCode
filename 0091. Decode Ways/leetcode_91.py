from functools import lru_cache

class Solution:
    @lru_cache
    def numDecodings(self, s: str) -> int:
        if s and s[0] == "0":
            return 0
        if len(s) <= 1:
            return 1
        elif 1 <= int(s[:2]) <= 26:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        elif 1 <= int(s[0]) <= 26:
            return self.numDecodings(s[1:])
        return 0
