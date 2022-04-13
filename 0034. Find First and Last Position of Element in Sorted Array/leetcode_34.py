from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findTarget(left, right, leftRightBound=None):
            res = [-1, -1]
            if left > right: return res
            mid = left + (right - left + 1) // 2
            if nums[mid] == target:
                if leftRightBound is None or leftRightBound == "L":
                    if mid == 0 or nums[mid - 1] < target:
                        res[0] = mid
                    else:
                        tempRes = findTarget(left, mid - 1, "L")
                        res[0] = tempRes[0]
                if leftRightBound is None or leftRightBound == "R":
                    if mid == len(nums) - 1 or nums[mid + 1] > target:
                        res[1] = mid
                    else:
                        tempRes = findTarget(mid + 1, right, "R")
                        res[1] = tempRes[1]
                return res
            elif nums[mid] > target and mid > 0:
                res = findTarget(left, mid - 1, leftRightBound)
            elif nums[mid] < target and mid < len(nums) + 1:
                res = findTarget(mid + 1, right, leftRightBound)
            return res

        return findTarget(0, len(nums) - 1)
