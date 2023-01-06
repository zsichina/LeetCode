class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def totalCost(digits, startAt):
            cost = pushCost * len(digits)
            for digit in digits:
                if digit != startAt:
                    cost += moveCost
                    startAt = digit
            return cost

        m, s = divmod(targetSeconds, 60)
        startAt = str(startAt)
        if m == 0 or s > 39:
            return totalCost(str(m * 100 + s), startAt)
        elif m > 99:
            return totalCost(str((m - 1) * 100 + s + 60), startAt)
        else:
            return min(
                totalCost(str(m * 100 + s), startAt),
                totalCost(str((m - 1) * 100 + s + 60), startAt),
            )


if __name__ == "__main__":
    sol = Solution()
    startAt = 1
    moveCost = 2
    pushCost = 1
    targetSeconds = 600
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 6)

    sol = Solution()
    startAt = 0
    moveCost = 9
    pushCost = 18
    targetSeconds = 460
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 81)

    startAt = 0
    moveCost = 1
    pushCost = 2
    targetSeconds = 6
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 3)

    startAt = 0
    moveCost = 1
    pushCost = 2
    targetSeconds = 76
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 6)

    startAt = 1
    moveCost = 9403
    pushCost = 9402
    targetSeconds = 6008
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 65817)

    startAt = 1
    moveCost = 9403
    pushCost = 9402
    targetSeconds = 5999
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 65817)

    startAt = 1
    moveCost = 9403
    pushCost = 9402
    targetSeconds = 4999
    print(sol.minCostSetTime(startAt, moveCost, pushCost, targetSeconds) == 75220)
