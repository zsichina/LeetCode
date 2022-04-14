class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combination(candidates: List[int], target: int):
            res = []
            prev = ""
            for idx, num in enumerate(candidates):
                if prev == num:
                    continue
                if target == num:
                    res += [[num]]
                if idx < len(candidates) - 1 and target-num >= candidates[idx+1]:
                    res += [[num] + x for x in self.combinationSum2(candidates[idx+1:], target-num)]
                prev = num
            return res

        candidates.sort()
        return combination(candidates, target)
