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


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache()
        def helper(idx, s, n):
            if idx == n:
                return 1
            elif idx > n or s[idx] == "0":
                return 0

            res = helper(idx + 1, s, n)
            if 0 < int(s[idx : idx + 2]) < 27:
                res += helper(idx + 2, s, n)
            return res

        return helper(0, s, len(s))


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1 : i + 1])
            if two_digit >= 10 and two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back
