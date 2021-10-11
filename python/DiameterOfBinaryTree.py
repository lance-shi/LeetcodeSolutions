# Question No. 543
# Diameter of Binary Tree
# Initial solution
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        length, diameter = self.get_length_and_diameter(root)
        return diameter

    def get_length_and_diameter(self, root):
        if root.left == None and root.right == None:
            return (0, 0)
        right_length = right_diameter = left_length = left_diameter = 0
        branches = 0
        if root.left != None:
            left_length, left_diameter = self.get_length_and_diameter(root.left)
            branches += 1
        if root.right != None:
            right_length, right_diameter = self.get_length_and_diameter(root.right)
            branches += 1

        length = max(left_length, right_length) + 1
        diameter = max(left_length + right_length + branches, left_diameter, right_diameter)
        return (length, diameter)