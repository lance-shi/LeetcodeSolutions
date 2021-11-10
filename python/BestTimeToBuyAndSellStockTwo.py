class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        hold = False
        n = len(prices)
        buy = 0
        for i in range(n):
            if not hold:
                if i < n - 1 and prices[i] <= prices[i + 1]:
                    buy = prices[i]
                    hold = True
                    continue
            if hold:
                if i == n - 1 or prices[i] > prices[i + 1]:
                    p += prices[i] - buy
                    hold = False
        return p