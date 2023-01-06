from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque()
        level = 1
        q.append((root, level))
        sm, cnt = 0, 0

        while q:
            node, lvl = q.popleft()
            if lvl > level:
                level += 1
                res.append(round(sm / cnt, 5))
                sm = 0
                cnt = 0

            sm += node.val
            cnt += 1

            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))

        res.append(round(sm / cnt, 5))

        return res
