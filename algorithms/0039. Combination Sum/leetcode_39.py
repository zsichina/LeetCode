from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        for idx, num in enumerate(candidates):
            if target % num == 0:
                res += [[num] * (target // num)]
            if idx < len(candidates) - 1:
                for i in range(1, target // num):
                    res += [[num] * i + x for x in self.combinationSum(candidates[idx + 1 :], target - num * i)]
        return res
