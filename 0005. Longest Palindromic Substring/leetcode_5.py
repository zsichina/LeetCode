class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end, sLen = 0, 0, len(s)

        def expandAroundCenter(s, left, right):
            while left >= 0 and right < sLen and s[left] == s[right]:
                left = left - 1
                right = right + 1
            return right - left - 1

        for i in range(sLen):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start: end + 1]

