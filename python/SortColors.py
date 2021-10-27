# Question No. 75
# Sort Colors
# Original solution
class Solution:
    def sortColors(self, nums) -> None:
        r = g = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                r += 1
                if nums[r - 1] > 0:
                    nums[r - 1], nums[i] = nums[i], nums[r - 1]
                if g != 0:
                    nums[r + g - 1], nums[i] = nums[i], nums[r + g - 1]
                continue
            if nums[i] == 1:
                g += 1
                if nums[r + g - 1] > 1:
                    nums[r + g - 1], nums[i] = nums[i], nums[r + g - 1]