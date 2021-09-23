class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxCons = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                if current > maxCons:
                    maxCons = current
            else:
                current = 0
        return maxCons