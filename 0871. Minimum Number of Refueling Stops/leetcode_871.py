from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h = []
        heapify(h)
        fuel = startFuel
        cnt = 0
        for i in range(len(stations)):
            
            fuel -= stations[i][0] if i == 0 else stations[i][0] - stations[i-1][0]

            while h and fuel < 0:
                fuel -= heappop(h)
                cnt += 1

            if fuel < 0:
                return -1
            
            heappush(h, -stations[i][1])

        fuel -= target - stations[-1][0] if stations else target

        while h and fuel < 0:
            fuel -= heappop(h)
            cnt += 1

        if fuel < 0:
            return -1

        return cnt
