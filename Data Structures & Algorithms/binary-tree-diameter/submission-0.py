# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        def getHeight(node):
            if not node:
                return 0
            lH = getHeight(node.left)
            rH = getHeight(node.right)
            curH = lH + rH
            self.maxDiameter = max(curH, self.maxDiameter)

            return 1 + max(lH, rH)

        getHeight(root)
        return self.maxDiameter