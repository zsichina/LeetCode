from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in range(len(strs)):
            res[tuple(sorted(strs[i]))].append(strs[i])
        return res.values()
