# Question No. 540
# Single Element in a Sorted Array
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        def findNonDup(l, r):
            nonlocal nums
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid - 1] == nums[mid]:
                if mid % 2 == 0:
                    return findNonDup(l, mid - 2)
                else:
                    return findNonDup(mid + 1, r)
            elif nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    return findNonDup(mid + 2, r)
                else:
                    return findNonDup(l, mid - 1)
            else:
                return nums[mid]
        return findNonDup(0, n - 1)