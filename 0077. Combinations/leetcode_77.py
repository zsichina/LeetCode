from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(start, k):
            if k == 0:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, k - 1)
                comb.pop()

        backtrack(1, k)

        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        dp = {}

        def backtrack(m, l):
            if k == l:
                if not (m, n + 1) in dp:
                    dp[(m, n + 1)] = [[x] for x in range(m, n + 1)]
                return dp[(m, n + 1)]
            else:
                res = []
                for i in range(m, n + 1):
                    if not (i + 1, l + 1) in dp:
                        dp[(i + 1, l + 1)] = backtrack(i + 1, l + 1)
                    res += [[i] + x for x in dp[(i + 1, l + 1)]]
                return res

        ans += backtrack(1, 1)

        return ans
