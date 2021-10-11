# Question No. 543
# Diameter of Binary Tree
# After reading discussions solution
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        diameter = 0
        def height(root):
            nonlocal diameter
            if root == None:
                return 0
            left = height(root.left)
            right = height(root.right)
            diameter = max(left + right, diameter)
            return max(left, right) + 1
        height(root)
        return diameter