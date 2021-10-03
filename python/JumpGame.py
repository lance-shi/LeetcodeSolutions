# Question No. 55
# Jump Game
class Solution:
    def canJump(self, nums):
        possibleReach = 0
        for i, num in enumerate(nums):
            if i > possibleReach:
                return False
            possibleReach = max(possibleReach, i + num)
            if possibleReach >= len(nums):
                return True
        return True
        