from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bounds(start, end, find_left = True):
            
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    if find_left:
                        if mid == 0 or nums[mid-1] != target:
                            return mid
                        end = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid+1] != target:
                            return mid
                        start = mid + 1
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return -1
        
        left = find_bounds(0, len(nums) - 1)
        
        if left == -1:
            return [-1,-1]
        
        right = find_bounds(left, len(nums) - 1, False)
        
        return [left, right]
