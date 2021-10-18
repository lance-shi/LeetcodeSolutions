# Question No. 993
# Cousins in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        cur_queue = [root]
        found = False
        parent_val = 0
        while len(cur_queue) > 0:
            next_queue = []
            for node in cur_queue:
                if node.left != None:
                    if node.left.val == x or node.left.val == y:
                        if found:
                            if parent_val != node.val:
                                return True
                            else:
                                return False
                        else:
                            found = True
                            parent_val = node.val
                    else:
                        next_queue.append(node.left)
                if node.right != None:
                    if node.right.val == x or node.right.val == y:
                        if found:
                            if parent_val != node.val:
                                return True
                            else:
                                return False
                        else:
                            found = True
                            parent_val = node.val
                    else:
                        next_queue.append(node.right)
            if found:
                return False
            cur_queue = next_queue
        return False

