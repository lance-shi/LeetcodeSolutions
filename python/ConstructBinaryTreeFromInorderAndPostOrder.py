# Question No. 106
# Construct Binary Tree from Inorder and Postorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        def construct(istart, iend, pstart, pend):
            val = postorder[pend]
            root = TreeNode(val)
            for i in range(istart, iend + 1):
                if inorder[i] == val:
                    break
            if i > istart:
                root.left = construct(istart, i - 1, pstart, pstart + i - 1 - istart)
            if i < iend:
                root.right = construct(i + 1, iend, pstart + i - istart ,pend - 1)
            return root
        return construct(0, len(inorder) - 1, 0, len(inorder) - 1)

