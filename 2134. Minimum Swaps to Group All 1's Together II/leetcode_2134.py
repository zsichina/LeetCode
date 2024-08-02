from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n, ones = len(nums), sum(nums)
        sm = mx = sum(nums[:ones])
        for i in range(1, n):
            sm += nums[(i + ones - 1) % n]
            sm -= nums[i - 1]
            mx = max(sm, mx)
        return ones - mx
