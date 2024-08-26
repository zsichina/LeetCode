from ast import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []
        if not root:
            return res
        for node in root.children:
            res.extend(self.postorder(node))

        return res + [root.val]
