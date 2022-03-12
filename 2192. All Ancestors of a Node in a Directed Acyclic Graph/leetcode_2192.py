from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        @lru_cache(None)
        def getAllAncestors(num):
            st = set(parents[num])
            for val in parents[num]:
                st.update(getAllAncestors(val))
            return st

        ans = []
        parents = defaultdict(list)
        for x, y in edges:
            parents[y].append(x)

        for i in range(n):
            ans.append(sorted(list(getAllAncestors(i))))

        return ans