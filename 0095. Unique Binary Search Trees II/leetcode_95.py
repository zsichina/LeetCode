from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def builTrees(vals: List[int]) -> List[TreeNode]:
            if len(vals) == 0:
                return [None]
            out = []
            for i in range(len(vals)):
                leftrees = builTrees(vals[:i])
                rightrees = builTrees(vals[i+1:])
                for lt in leftrees:
                    for rt in rightrees:
                        out.append(TreeNode(vals[i], lt, rt))
            return out
        return builTrees([x for x in range(1, n+1)])
