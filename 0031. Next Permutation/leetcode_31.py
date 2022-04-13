from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        maxIdx = len(nums)-1
        for i in range(len(nums) -1, 0, -1):
            if nums[i] > nums[maxIdx]:
                maxIdx = i
            low = maxIdx
            if nums[maxIdx] > nums[i-1]:
                for j in range(len(nums)-i):
                    if nums[i+j] > nums[i-1] and nums[i+j] < nums[low]:
                        low = i+j
                nums[low], nums[i-1] = nums[i-1], nums[low]
                nums[i:] = sorted(nums[i:])
                return

        nums.sort()
