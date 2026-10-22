class Solution:
    def maxProfit(self, prices):
        maxprofit=0
        minprofit=float("inf")
        n=len(prices)
        for i in range(0,n):
            minprofit=min(minprofit,prices[i])
            maxprofit=max(maxprofit,prices[i]-minprofit)
        return maxprofit