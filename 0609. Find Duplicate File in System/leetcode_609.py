from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dp = defaultdict(list)
        for path in paths:
            path_lst = path.split()
            for filename in path_lst[1:]:
                name, content = filename.split("(")
                dp[content].append(path_lst[0] + "/" + name)

        res = []
        for _, val in dp.items():
            if len(val) > 1:
                res.append(val)

        return res
