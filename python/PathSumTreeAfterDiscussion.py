# Question No. 437
# Path Sum three
# Solution after reading discussions
from Collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        result = 0
        sum_list = defaultdict(int)
        sum_list[0] = 1
        def cal_sum(root, total):
            nonlocal result, targetSum
            if root == None:
                return
            total += root.val
            
            result += sum_list[total - targetSum]
            sum_list[total] += 1
            cal_sum(root.left, total)
            cal_sum(root.right, total)
            sum_list[total] -= 1
        cal_sum(root, 0)
        return result
        