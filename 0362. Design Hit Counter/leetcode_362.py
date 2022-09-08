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
