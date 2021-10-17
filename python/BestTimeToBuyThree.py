# Question No. 123
# Best Time to Buy and Sell Stock Three
class Solution:
    def maxProfit(self, prices) -> int:
        buy_list = []
        sell_list = []
        holding = False
        n = len(prices)
        for i in range(n):
            if not holding:
                if i + 1 < n and prices[i + 1] > prices[i]:
                    buy_list.append(prices[i])
                    holding = True
            else:
                if i + 1 == n or prices[i + 1] < prices[i]:
                    sell_list.append(prices[i])
                    holding = False
        n = len(buy_list)
        if n == 0:
            return 0
        if n == 1:
            return sell_list[0] - buy_list[0]

        min_buy_prices = [buy_list[0] for i in range(n)]
        for i in range(1, n):
            min_buy_prices[i] = min(min_buy_prices[i - 1], buy_list[i])
        max_sell_prices = [sell_list[-1] for i in range(n)]
        for i in range(n - 2, -1, -1):
            max_sell_prices[i] = max(max_sell_prices[i + 1], sell_list[i])
        max_buy_profit = [(sell_list[-1] - buy_list[-1]) for i in range(n)]
        for i in range(n - 2, -1, -1):
            max_buy_profit[i] = max(max_sell_prices[i] - buy_list[i], max_buy_profit[i + 1])
        max_sell_profit = [(sell_list[0] - buy_list[0]) for i in range(n)]
        for i in range(1, n):
            max_sell_profit[i] = max(sell_list[i] - min_buy_prices[i], max_sell_profit[i - 1])
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, max_sell_profit[i - 1] + max_buy_profit[i])
        return max_profit