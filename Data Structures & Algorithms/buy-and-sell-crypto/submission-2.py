class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy, sell = 0, 1
        res = 0

        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                res = max(res, profit)
            sell += 1

        return res
