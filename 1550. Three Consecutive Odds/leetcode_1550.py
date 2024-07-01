from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_cnt = 0
        for elem in arr:
            if elem % 2 == 1:
                odd_cnt += 1
                if odd_cnt == 3:
                    return True
            else:
                odd_cnt = 0
        return False
