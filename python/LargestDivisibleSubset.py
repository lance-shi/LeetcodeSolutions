# Question No. 368
# Largest Divisible Subset
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1 for i in range(n)]
        pre = [-1 for i in range(n)]
        max_num = 1
        max_index = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    pre[i] = j
                    if dp[i] > max_num:
                        max_num = dp[i]
                        max_index = i
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = pre[max_index]
        return result