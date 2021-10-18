# Question No. 437
# Path Sum three
# Original Solution
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        result = 0
        def cal_sum(root, target, is_original):
            nonlocal result
            if root == None:
                return
            if root.val == target:
                result += 1
            remains = target - root.val
            cal_sum(root.left, remains, False)
            cal_sum(root.right, remains, False)
            if is_original:
                cal_sum(root.left, target, True)
                cal_sum(root.right, target, True)
        cal_sum(root, targetSum, True)
        return result
        