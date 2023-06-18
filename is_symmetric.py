from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None or right is None:
            return left is right
        if left.val != right.val:
            return False

        return self.checkSymmetry(left.left, right.right) and self.checkSymmetry(left.right, right.left)
