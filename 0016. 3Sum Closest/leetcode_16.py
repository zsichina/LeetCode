from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        i,j,k = 0,1,len(nums)-1
        nums.sort()
        closest = 10**5
        sm = 0

        while i < len(nums)-1:
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 > target:
                    k+=-1
                elif sum3 < target:
                    j += 1
                else:
                    return sum3

                if abs(target - sum3) < closest:
                    closest = abs(target - sum3)
                    sm = sum3
            i += 1
            j = i + 1
            k = len(nums) - 1

        return sm
