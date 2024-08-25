from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_profits = [0 for _ in range(n)]
        right_profits = [0 for _ in range(n + 1)]
        min_left, max_right = prices[0], prices[-1]
        for i in range(1, n):
            min_left = min(min_left, prices[i])
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_left)
            max_right = max(max_right, prices[n - 1 - i])
            right_profits[n - 1 - i] = max(right_profits[n - i], max_right - prices[n - 1 - i])

        max_total = 0
        for i in range(n):
            max_total = max(max_total, left_profits[i] + right_profits[i + 1])

        return max_total
