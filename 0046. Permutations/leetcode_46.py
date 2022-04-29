from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1: return [nums]
        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]
        res = []
        for i in range(len(nums)):
            res += [[nums[i]] + x for x in self.permute(nums[0:i] + nums[i+1:])]
        return res
