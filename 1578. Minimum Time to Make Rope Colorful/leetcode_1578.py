from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        seq_sum, max_in_seq = neededTime[0], neededTime[0]
        n = len(colors)
        for i in range(1, n+1):
            if i == n or colors[i] != colors[i-1]:
                total += seq_sum-max_in_seq
                if i < n:
                    max_in_seq = neededTime[i]
                    seq_sum = neededTime[i]
            else:
                seq_sum += neededTime[i]
                max_in_seq = max(max_in_seq, neededTime[i])

        return total
