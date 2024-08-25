from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permuteSorted(nums):
            if len(nums) <= 1:
                return [nums]
            if len(nums) == 2:
                if nums[0] == nums[1]:
                    return [nums]
                return [nums, [nums[1], nums[0]]]
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                res += [[nums[i]] + x for x in permuteSorted(nums[0:i] + nums[i + 1 :])]
            return res

        nums.sort()
        res = permuteSorted(nums)
        return res
