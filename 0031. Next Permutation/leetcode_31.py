from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i+1] > nums[i]:
                max_idx = i+1
                for j in range(i+1, n):
                    if nums[j] > nums[i] and nums[j] < nums[max_idx]:
                        max_idx = j

                nums[max_idx], nums[i] = nums[i], nums[max_idx]
                nums[i+1:] = sorted(nums[i+1:])
                return

        nums.sort()
