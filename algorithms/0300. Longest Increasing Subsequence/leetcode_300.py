from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for x in range(len(nums))]
        max_length = 1
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            max_length = max(max_length, dp[i])
        return max_length
