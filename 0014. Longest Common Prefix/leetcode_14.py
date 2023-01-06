from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommon(pref):
            for val in strs:
                if not val.startswith(pref):
                    return False
            return True

        prefix = min(strs, key=len)
        if len(strs) == 0:
            return prefix

        while prefix:
            if isCommon(prefix):
                return prefix
            else:
                prefix = prefix[:-1]

        return prefix
