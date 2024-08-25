from collections import defaultdict
from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = defaultdict(int)
        maxVal = 0
        ans = -1
        for i in range(len(nums) - 1):
            if nums[i] == key:
                d[nums[i + 1]] += 1
                if d[nums[i + 1]] > maxVal:
                    maxVal = d[nums[i + 1]]
                    ans = nums[i + 1]
        return ans
