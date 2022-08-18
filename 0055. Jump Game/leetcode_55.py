from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        steps = nums[0]
        n = len(nums)
        while steps and curr < n-1:
            curr+=1
            steps -= 1
            if nums[curr] > steps:
                steps = nums[curr]        
        return curr == n-1


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        steps = 0
        for idx in range(n):
            steps = max(steps, nums[idx])
            if steps == 0:
                break
            # if idx + steps >= n-1:
            #     return True
            steps -= 1
        
        return idx == n-1
