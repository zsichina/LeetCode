from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def findTarget(left, right):
            res = -1
            mid = left + (right - left + 1) // 2
            if target > nums[mid]:
                if mid == right:
                    res = right + 1
                else:
                    res = findTarget(mid + 1, right)
            elif target < nums[mid]:
                if mid == left:
                    res = left
                else:
                    res = findTarget(left, mid - 1)
            else:
                res = mid
            return res

        return findTarget(0, len(nums) - 1)
