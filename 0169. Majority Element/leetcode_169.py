from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key, val in counter.items():
            if val > len(nums) / 2:
                return key
        return 0


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v > len(nums) / 2][0]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, cnt = nums[0], 1
        for num in nums[1:]:
            if cnt == 0 or num == candidate:
                candidate = num
                cnt += 1
            else:
                cnt -= 1
        return candidate
