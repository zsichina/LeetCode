from typing import List
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end, sm, min_len, n = 0, 0, 0, math.inf, len(nums)
        while start < len(nums):
            if sm < target:
                if end == n:
                    break
                sm += nums[end]
                end += 1
            else:
                sm -= nums[start]
                start += 1

            if sm >= target:
                min_len = min(min_len, end-start)

        return min_len if min_len < math.inf else 0
