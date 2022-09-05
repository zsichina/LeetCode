from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: return res

        level = 0
        q = deque([(root, level+1)])
        while q:
            node, lvl = q.popleft()
            if lvl > level:
                level += 1
                res.append([node.val])
            else:
                res[-1].append(node.val)

            for child in node.children:
                q.append([child, level+1])

        return res
