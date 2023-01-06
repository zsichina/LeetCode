from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dp = {}
        for i in range(len(nums)):
            if nums[i] in dp and abs(dp[nums[i]] - i) <= k:
                return True
            dp[nums[i]] = i
        return False
