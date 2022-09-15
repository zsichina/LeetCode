from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if not n or n%2 == 1:
            return []

        changed.sort()
        dp = {}

        for i in range(n):
            if changed[i] not in dp:
                dp[changed[i]] = 1
            else:
                dp[changed[i]] += 1

        res = []
        for i in range(n):
            if dp[changed[i]] == 0:
                continue

            dp[changed[i]] -= 1
            if changed[i]*2 not in dp or dp[changed[i]*2] == 0:
                return []
            else:
                dp[changed[i]*2] -= 1
                res.append(changed[i])

        return res
