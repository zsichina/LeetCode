from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx, max_profit = 0, 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_idx]:
                min_idx = i
            else:
                max_profit = max(max_profit, prices[i] - prices[min_idx])

        return max_profit
