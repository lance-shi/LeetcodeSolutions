# Question No. 2012
# Sum of Beauty in the Array
class Solution:
    def sumOfBeauties(self, nums) -> int:
        N = len(nums)
        max_list = [0 for i in range(N)]
        min_list = [0 for i in range(N)]
        max_list[0] = nums[0]
        min_list[-1] = nums[-1]
        for i in range(1, N - 2):
            max_list[i] = max(max_list[i - 1], nums[i])
        for i in range(1, N - 2):
            min_list[N - i - 1] = min(min_list[N - i], nums[N - i - 1])
        sum_beauties = 0
        for i in range(1, N - 1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                sum_beauties += 1
                if max_list[i - 1] < nums[i] < min_list[i + 1]:
                    sum_beauties += 1
        return sum_beauties