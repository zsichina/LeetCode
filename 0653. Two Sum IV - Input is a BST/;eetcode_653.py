from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dp = set()

        def dfs(root):
            if root.val in dp:
                return True

            dp.add(k - root.val)

            if root.left and dfs(root.left):
                return True

            if root.right and dfs(root.right):
                return True

            return False

        return dfs(root)


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dp = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val in dp:
                return True

            dp.add(k - node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        dp = set()
        de = deque([root])
        while de:
            node = de.popleft()
            if node.val in dp:
                return True

            dp.add(k - node.val)

            if node.left:
                de.append(node.left)

            if node.right:
                de.append(node.right)

        return False
