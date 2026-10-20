class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        minProfit = float("inf")
        n = len(prices)

        for i in range(n):
            minProfit = min(minProfit, prices[i])
            maxProfit = max(maxProfit, prices[i] - minProfit)

        return maxProfit