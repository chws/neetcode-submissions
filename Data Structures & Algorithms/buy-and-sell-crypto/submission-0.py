class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointer: move right, and update left when right val is smaller than left val
        # save the min val among the left bracket while moving right, and calculate max profit every move
        n = len(prices)
        left = 0
        max_profit = 0
        for right in range(n):
            if prices[left] < prices[right]:
                max_profit = max(max_profit, prices[right]-prices[left])
            else:
                left = right
        return max_profit