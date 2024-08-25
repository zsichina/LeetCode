from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        start, end = 0, n
        for i in range(n):
            if newInterval[0] > intervals[i][1]:
                start += 1
            if newInterval[1] < intervals[n - 1 - i][0]:
                end -= 1

        if start == end:
            intervals.insert(start, newInterval)
            return intervals

        intervals[start:end] = [
            [
                min(intervals[start][0], newInterval[0]),
                max(intervals[end - 1][1], newInterval[1]),
            ]
        ]

        return intervals
