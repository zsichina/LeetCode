from ctypes import pointer
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        slow, cnt = 1, 1
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[slow] = nums[fast]
                slow += 1

        return slow
