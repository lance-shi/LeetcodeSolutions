# Question No. 300
# Longest Increasing Subsequence
# d represents the smallest number of each length at current stage
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums) -> int:
        d = [nums[0]]
        cur_len = 1
        for i in range(1, len(nums)):
            if nums[i] > d[cur_len - 1]:
                cur_len += 1
                d.append(nums[i])
            else:
                index = bisect_left(d, nums[i])
                d[index] = nums[i]

        return cur_len