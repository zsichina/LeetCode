from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        red_pointer, white_pointer = 0, 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[red_pointer] = nums[red_pointer], nums[i]
                red_pointer += 1
                white_pointer = max(red_pointer, white_pointer)
            if nums[i] == 1:
                nums[i], nums[white_pointer] = nums[white_pointer], nums[i]
                white_pointer += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        pointer = 0
        while pointer <= right:
            if nums[pointer] == 0:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                pointer += 1
                left += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:
                pointer += 1
