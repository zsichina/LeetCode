import math
from collections import defaultdict, deque
from typing import List, Optional


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
                dfs(root.left, row + 1, col - 1)

            if root.right:
                dfs(root.right, row + 1, col + 1)

        d = defaultdict(list)
        start, end = 0, 0

        dfs(root, 0, 0)

        res = []
        for i in range(start, end + 1):
            d[i] = sorted(d[i], key=lambda x: (x[0], x[1]))
            res.append([x[1] for x in d[i]])

        return res


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, row, col):
            lst.append((col, row, root.val))

            if root.left:
                dfs(root.left, row + 1, col - 1)

            if root.right:
                dfs(root.right, row + 1, col + 1)

        lst = []
        dfs(root, 0, 0)

        lst.sort()

        res = []
        prev_col = -math.inf
        for i in range(len(lst)):
            if lst[i][0] != prev_col:
                res.append([lst[i][2]])
                prev_col = lst[i][0]
            else:
                res[-1].append(lst[i][2])

        return res


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root):
            q = deque([(root, 0, 0)])
            while q:
                node, row, col = q.popleft()
                lst.append((col, row, node.val))

                if node.left:
                    q.append((node.left, row + 1, col - 1))

                if node.right:
                    q.append((node.right, row + 1, col + 1))

        lst = []
        bfs(root)

        lst.sort()

        res = []
        prev_col = -math.inf
        for i in range(len(lst)):
            if lst[i][0] != prev_col:
                res.append([lst[i][2]])
                prev_col = lst[i][0]
            else:
                res[-1].append(lst[i][2])

        return res
