from heapq import (
    heappop,
    heappush,
)
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-(10**4) - 1] * k
        for num in nums:
            if self.heap[0] < num:
                heappop(self.heap)
                heappush(self.heap, num)

    def add(self, val: int) -> int:
        if self.heap[0] < val:
            heappop(self.heap)
            heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
