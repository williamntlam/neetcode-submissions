class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window.
        left = 0
        profit = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            
            profit = max(profit, prices[right] - prices[left])

        return profit