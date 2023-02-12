import math
from collections import defaultdict
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if len(roads) == 0:
            return 0
        dp, seen, total_fuel = defaultdict(list), set(), 0
        for p, c in roads:
            dp[p].append(c)
            dp[c].append(p)

        def dfs(city):
            nonlocal total_fuel
            seen.add(city)
            total_reps = 1
            for neibour in dp[city]:
                if neibour not in seen:
                    reps = dfs(neibour)
                    total_fuel += math.ceil(reps / seats)
                    total_reps += reps

            return total_reps

        dfs(0)

        return total_fuel
