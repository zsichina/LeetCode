class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9+7
        dp = {}
        def rec(dice_index, n, curr_sum, target, k):
            if dice_index == n:
                return int(curr_sum == target)

            if (dice_index, curr_sum) in dp:
                return dp[(dice_index, curr_sum)]

            cnt = 0
            for i in range(1, min(k, target-curr_sum)+1):
                cnt = (cnt + rec(dice_index+1, n, curr_sum+i, target, k))%MOD

            dp[(dice_index, curr_sum)] = cnt

            return dp[(dice_index, curr_sum)]
        
        return rec(0, n, 0, target, k)
