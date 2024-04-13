# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1189415684/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # buy, sell
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit
            else:
                left = right
            right += 1

        return max_profit
