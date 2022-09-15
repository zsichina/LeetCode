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


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if not n or n%2 == 1:
            return []

        min_val, max_val = min(changed), max(changed)
        dp = [0 for _ in range(max_val-min_val+1)]

        for val in changed:
            dp[val-min_val] += 1

        res = []
        for i in range(len(dp)):
            while dp[i] > 0:
                dp[i] -= 1
                if (i+min_val)*2 > max_val or dp[(i+min_val)*2-min_val] == 0:
                    return []
                else:
                    res.append(i+min_val)
                    dp[(i+min_val)*2-min_val] -= 1

        return res
