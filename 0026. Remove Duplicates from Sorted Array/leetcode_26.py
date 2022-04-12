from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        curr = 0
        for j in range(1, len(nums)):
            if nums[curr] != nums[j]:
                curr += 1
                nums[curr], nums[j] = nums[j], nums[curr]

        return curr + 1
