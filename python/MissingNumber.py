# Question No. 268
# Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        return ((max_num + 1) * max_num) // 2 - sum(nums)