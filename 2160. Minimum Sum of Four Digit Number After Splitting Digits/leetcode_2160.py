class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(list(str(num)))
        return int(nums[0] + nums[3]) + int(nums[1] + nums[2])
