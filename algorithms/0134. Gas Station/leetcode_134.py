from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = end = curr_tank = 0
        for _ in range(n):
            if curr_tank + gas[end] - cost[end] >= 0:
                curr_tank += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                curr_tank += gas[start] - cost[start]

        return -1 if curr_tank < 0 else (n + start) % n
