# Question No. 55
# Jump Game
class Solution:
    def canJump(self, nums):
        possibleReach = 0
        for i in range(len(nums)):
            if i > possibleReach:
                return False
            possibleReach = max(possibleReach, i + nums[i])
            if possibleReach >= len(nums):
                return True
        return True
        