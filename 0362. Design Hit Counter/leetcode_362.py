from collections import deque
import bisect


class HitCounter:

    def __init__(self):
        self.timestamps = [0]
        self.total_hits = [0]


    def hit(self, timestamp: int) -> None:
        if self.timestamps[-1] == timestamp:
            self.total_hits[-1] += 1
        else:
            self.timestamps.append(timestamp)
            self.total_hits.append(self.total_hits[-1] + 1)


    def getHits(self, timestamp: int) -> int:
        end = bisect.bisect(self.timestamps, timestamp) - 1
        start = bisect.bisect(self.timestamps, max(0, timestamp-300)) - 1

        return self.total_hits[end] - self.total_hits[start]


class HitCounter:

    def __init__(self):
        self.hits = deque()
        self.total = 0


    def hit(self, timestamp: int) -> None:
        self.total += 1
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1


    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            hits = self.hits.popleft()
            self.total -= hits[1]

        return self.total
