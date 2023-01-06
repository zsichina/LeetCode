from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        sm = int(k * (k + 1) / 2)
        # if k < min(nums): return sm
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            elif nums[i] <= k:
                k += 1
                sm = sm + k - nums[i]
            else:
                break
        return sm
