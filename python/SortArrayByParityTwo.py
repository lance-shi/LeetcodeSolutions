class Solution:
    def sortArrayByParityII(self, nums):
        i = 0
        j = 1
        N = len(nums)
        while True:
            while i < N and nums[i] % 2 == 0:
                i += 2
            while j < N and nums[j] % 2:
                j += 2
            if i >= N or j >= N:
                break
            nums[i], nums[j] = nums[j], nums[i]
        return nums