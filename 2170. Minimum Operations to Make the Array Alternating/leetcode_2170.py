import math
from collections import Counter
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        length = len(nums)
        minSteps = math.inf

        for evenKey, evenVal in Counter(nums[::2]).most_common(2):
            for oddKey, oddVal in Counter(nums[1::2]).most_common(2):
                steps = length - evenVal if evenKey == oddKey else length - evenVal - oddVal
                minSteps = steps if steps < minSteps else minSteps
        return minSteps
