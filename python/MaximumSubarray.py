# Question No. 53
# Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -10001
        s = 0
        for num in nums:
            s += num
            m = max(m, s)
            s = max(0, s)
        return m