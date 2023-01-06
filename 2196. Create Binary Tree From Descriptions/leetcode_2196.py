from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = set()
        children = set()
        desc = defaultdict()
        for p, c, lr in descriptions:
            parents.add(p)
            children.add(c)
            if p not in desc:
                desc[p] = TreeNode(p)
            if c not in desc:
                desc[c] = TreeNode(c)
            if lr == 1:
                desc[p].left = desc[c]
            else:
                desc[p].right = desc[c]

        return desc[list(parents.difference(children))[0]]
