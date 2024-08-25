from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(left, right):
            pivot = 0
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                pivot = findPivot(mid + 1, right)
            elif nums[mid] < nums[right]:
                pivot = findPivot(left, mid)
            else:
                return mid
            return pivot

        def findTarget(left, right):
            if left > right:
                return -1
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return findTarget(mid + 1, right)
            else:
                return findTarget(left, mid - 1)

        pivot = findPivot(0, len(nums) - 1)

        if target == nums[pivot]:
            return pivot
        elif target <= nums[-1]:
            return findTarget(pivot, len(nums) - 1)
        else:
            return findTarget(0, pivot - 1)
