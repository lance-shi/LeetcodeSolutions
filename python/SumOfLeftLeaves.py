# Question No. 404
# Sum of Left Leaves
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        self.dfs(root, False)
        return self.sum

    def dfs(self, root, is_left):
        if not root:
            return
        if not root.left and not root.right:
            if is_left:
                self.sum += root.val
            return
        self.dfs(root.left, True)
        self.dfs(root.right, False)