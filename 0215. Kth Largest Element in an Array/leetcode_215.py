from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num, max_num = min(nums), max(nums)
        counting = [0 for _ in range(max_num-min_num+2)]
        for num in nums:
            counting[num-min_num] += 1

        start = max_num-min_num
        while k > 0:
            k -= counting[start]
            start -= 1

        return start+1+min_num
