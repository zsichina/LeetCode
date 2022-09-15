class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dp = {}
        fast, slow, cnt, max_len, n = 0, 0, 0, 0, len(s)
        while fast < n:
            if s[fast] not in dp or dp[s[fast]] == 0:
                dp[s[fast]] = 1
                cnt += 1
            else:
                dp[s[fast]] += 1

            while cnt > 2:
                dp[s[slow]] -= 1
                if dp[s[slow]] == 0:
                    cnt -= 1
                slow += 1

            fast += 1
            max_len = max(max_len, fast-slow)

        return max_len
