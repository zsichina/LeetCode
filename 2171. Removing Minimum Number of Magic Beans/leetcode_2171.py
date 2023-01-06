from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        maxRemaining = 0
        for i, val in enumerate(sorted(beans)):
            maxRemaining = max(val * (n - i), maxRemaining)
        return sum(beans) - maxRemaining
