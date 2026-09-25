class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        L = 0
        R = 1
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maxp = max(maxp, profit)
            else:
                L = R
            R += 1
            
        return maxp