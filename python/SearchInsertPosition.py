# Question No. 35
# Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def b_search(start, end):
            if target <= nums[start]:
                return start
            if target > nums[end]:
                return end + 1
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return b_search(start, mid - 1)
            return b_search(mid + 1, end)
        return b_search(0, n - 1)