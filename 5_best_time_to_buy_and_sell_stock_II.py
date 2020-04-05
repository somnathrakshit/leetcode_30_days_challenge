# Title: Best Time to Buy and Sell Stock II
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                total += prices[i+1] - prices[i]
        return total
