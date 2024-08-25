from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cnt = 0
        nums.sort()

        for i in range(n):
            start, end = i + 1, n - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] < target:
                    cnt += end - start
                    start += 1
                else:
                    end -= 1

        return cnt
