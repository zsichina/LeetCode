import heapq
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        cnt = 0
        while costs and costs[0] <= coins:
            cnt += 1
            coins -= heapq.heappop(costs)

        return cnt
