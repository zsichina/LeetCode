from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        dp = {}
        for idx, source, target in zip(indices, sources, targets):
            length = len(source)
            if s[idx:idx+length] == source:
                dp[idx] = (length, target)

        res = []
        str_idx, str_len = 0, len(s)
        while str_idx < str_len:
            if str_idx not in dp:
                res.append(s[str_idx])
                str_idx += 1
            else:
                res.append(dp[str_idx][1])
                str_idx += dp[str_idx][0]

        return "".join(res)
