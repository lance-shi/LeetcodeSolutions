# Question No. 154
# Find Minimum in Rotated Sorted Array Two
# Resolved with three different solutions
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        def searchMin(l, r):
            nonlocal nums
            if l == r:
                return nums[l]
            if r == l + 1:
                return min(nums[r], nums[l])
            if nums[l] < nums[r]:
                return nums[l]
            if nums[l] == nums[r]:
                l += 1
            else:
                mid = (l + r) // 2
                if num[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            return searchMin(l, r)
        return searchMin(l, r)

    #Linear solution
    def findMinLinear(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return nums[i]
            return nums[0]

    #Easiest
    def findMinLinearEasiest(self, nums: List[int]) -> int:
        return min(nums)