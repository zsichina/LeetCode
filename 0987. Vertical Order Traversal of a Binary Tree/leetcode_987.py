from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, row, col):
            nonlocal start, end
            start = min(start, col)
            end = max(end, col)

            d[col].append([row, root.val])

            if root.left:
                dfs(root.left, row+1, col-1)

            if root.right:
                dfs(root.right, row+1, col+1)


        d = defaultdict(list)
        start, end = 0, 0

        dfs(root, 0, 0)

        res = []
        for i in range(start, end+1):
            d[i] = sorted(d[i], key=lambda x: (x[0], x[1]))
            res.append([x[1] for x in d[i]])

        return res
