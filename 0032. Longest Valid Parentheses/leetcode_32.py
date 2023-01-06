class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0

        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right and 2 * left > longest:
                longest = 2 * left
            elif right > left:
                left = right = 0

        left = right = 0
        for c in s[::-1]:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right and 2 * left > longest:
                longest = 2 * left
            elif right < left:
                left = right = 0

        return longest
