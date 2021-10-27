# Question No. 75
# Sort Colors
# After reading comments I realized two pointers don't need to both start from beginning
# Both solutions are of similar efficiency, but this one is much easier to write
class Solution:
    def sortColors(self, nums) -> None:
        r = b = i = 0
        n = len(nums)
        while i + b < n:
            if nums[i] == 0:
                if i > r:
                    nums[r], nums[i] = nums[i], nums[r]
                r += 1
            if nums[i] == 2:
                if n - b - 1 > i:
                    nums[n - b - 1], nums[i] = nums[i], nums[n - b - 1]
                b += 1
                continue
            i += 1
