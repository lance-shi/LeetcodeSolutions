# Question No. 1413
# Minimum Value to Get Positive Step by Step Sum
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = cur = nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            m = min(m, cur)
        if m >= 0:
            return 1
        return -m + 1