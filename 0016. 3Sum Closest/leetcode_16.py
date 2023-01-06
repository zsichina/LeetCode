import math
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest = math.inf
        ans = 0
        for i in range(n):
            start, end = i + 1, n - 1
            while start < end:
                diff = nums[i] + nums[start] + nums[end] - target
                if abs(diff) < closest:
                    closest = abs(diff)
                    ans = nums[i] + nums[start] + nums[end]

                if diff < 0:
                    start += 1
                elif diff > 0:
                    end -= 1
                else:
                    break
        return ans
