# Question No. 1008
# Construct Binary Search Tree From Preorder Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        parent_queue = []
        cur_node = root
        for i in range(1, len(preorder)):
            new_val = preorder[i]
            new_node = TreeNode(new_val)
            if new_val < cur_node.val:
                parent_queue.append(cur_node)
                cur_node.left = new_node
            else:
                while len(parent_queue) > 0 and parent_queue[-1].val < new_val:
                    cur_node = parent_queue.pop()
                cur_node.right = new_node
            cur_node = new_node
        return root
