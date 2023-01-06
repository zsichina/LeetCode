from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm, maxSum = 0, -(10**4)
        for val in nums:
            sm += val
            maxSum = sm if sm > maxSum else maxSum
            sm = 0 if sm < 0 else sm
        return maxSum
