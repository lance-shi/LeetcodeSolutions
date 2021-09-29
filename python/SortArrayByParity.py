'''
Question 905: 
Sort Array By Parity
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''
# Two solutions for this question. Both runs 76ms

class Solution:
    def sortArrayByParity(self, nums):
        N = len(nums)
        i = 0
        j = N - 1
        while i < j:
            while i < N and nums[i] % 2 == 0:
                i += 1
            while j >= 0 and nums[j] % 2:
                j -= 1
            if i >= j:
                break
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def sortArrayByParityMethodTwo(self, nums):
	    odd = []
	    even = []
	    for num in nums:
	        if num % 2:
	            odd.append(num)
	        else:
	            even.append(num)
	    return even + odd