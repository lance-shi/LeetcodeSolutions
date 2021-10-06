# Question No.  442
# Find All Duplicates in an Array
# First solution is not O(1) space but faster
# Second one I got the idea from Discuss page

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        exist = [0 for i in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            exist[num] += 1
        result = []
        for i, val in enumerate(exist): 
            if val == 2:
                result.append(i)
        return result

    def findDuplicates2(self, nums: List[int]) -> List[int]:
        result = []
        for i, val in enumerate(nums): 
            value = abs(val)
            if nums[value - 1] < 0:
                result.append(value)
            else:
                nums[value - 1] = -nums[value - 1]
        return result
