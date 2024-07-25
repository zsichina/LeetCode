from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dct = Counter(nums)
        pointer = 0
        for key, val in sorted(dct.items(), key=lambda x: (x[1], -x[0])):
            nums[pointer : pointer + val] = [key for _ in range(val)]
            pointer += val

        return nums
