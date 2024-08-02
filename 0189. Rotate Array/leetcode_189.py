from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0:
            return
        temp = nums[:k]
        for i in range(n):
            temp[i % k], nums[(i + k) % n] = nums[(i + k) % n], temp[i % k]


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         k %= len(nums)

#         def reverse(left, right):
#             while left < right:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 left += 1
#                 right -= 1

#         reverse(0, len(nums) - 1)
#         reverse(0, k - 1)
#         reverse(k, len(nums) - 1)
