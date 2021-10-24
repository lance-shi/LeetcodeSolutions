# Question No. 222
# Count Complete Tree Nodes
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        depth = self.find_depth(root)
        if depth == 1:
            return 1
        self.total = [0, 1]
        for i in range(2, depth):
            self.total.append(self.total[-1] + 2 ** (i -1))
        print(self.total)
        return self.find_count(root, depth)

    def find_depth(self, root):
        temp = root
        count = 0
        while temp:
            temp = temp.left
            count += 1
        return count

    def find_count(self, root, depth):
        if not root:
            return 0
        if depth == 1:
            return 1
        left_depth = depth - 1
        right_depth = self.find_depth(root.right)
        if left_depth > right_depth:
            return 1 + self.total[right_depth] + self.find_count(root.left, left_depth)
        else:
            return 1 + self.total[left_depth] + self.find_count(root.right, right_depth)
        