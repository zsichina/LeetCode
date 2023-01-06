from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        lst = sorted(zip(growTime, plantTime), reverse=True)
        spent = rem = 0
        for g, p in lst:
            spent += p
            rem = max(0, rem - p)
            rem = max(rem, g)

        return spent + rem
