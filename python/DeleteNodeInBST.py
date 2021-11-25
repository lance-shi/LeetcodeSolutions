# Question No. 450
# Delete Node in a BST
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        tmp = root
        prev = None
        is_left = True
        while tmp != None:
            if tmp.val == key:
                break
            prev = tmp
            if key < tmp.val:
                tmp = tmp.left
                is_left = True
            else:
                tmp = tmp.right
                is_left = False
        if tmp == None:
            return root
        if tmp.left == None and tmp.right == None:
            if not prev:
                return None
            elif is_left:
                prev.left = None
            else:
                prev.right = None
            return root
        if tmp.left == None:
            if not prev:
                root = tmp.right
                return root
            if is_left:
                prev.left = tmp.right
            else:
                prev.right = tmp.right
            return root
        if tmp.right == None:
            if not prev:
                root = tmp.left
                return root
            if is_left:
                prev.left = tmp.left
            else:
                prev.right = tmp.left
            return root
        if not tmp.right.left:
            tmp.right.left = tmp.left
            if not prev:
                root = tmp.right
                return root
            if is_left:
                prev.left = tmp.right
            else:
                prev.right = tmp.right
            return root
        tmp2 = tmp.right
        while tmp2.left.left:
            tmp2 = tmp2.left
        tmp.val = tmp2.left.val
        tmp2.left = tmp2.left.right
        return root