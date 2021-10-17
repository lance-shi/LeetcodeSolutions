# Question No. 309
# Best Time to Buy and Sell Stock with Cooldown
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = b = c = 0
        for i in range(1, len(prices)):
            a, b, c = c, max(a, b) + prices[i] - prices[i - 1], max(a, b, c)
        return max(a, b, c)