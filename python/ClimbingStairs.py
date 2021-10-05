# Question No. 70
# Climbing Stairs
# This same code in two submissions result in 58ms and 28ms
# That proves that some time we don't need to strive too hard to a faster solutions
# If the complexity is in the best range, the answer should be good enough
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 1]
        for i in range(2, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]